package Server

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sync"

	"github.com/gorilla/websocket"
	"github.com/pion/webrtc/v3"
)

var AllRooms RoomMap

// WebSocket upgrader
var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

// Mutex to ensure WebRTC operations are thread-safe
var webrtcMutex sync.Mutex

// Handler to create a new WebRTC room
func CreateRoomRequestHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	roomID := AllRooms.CreateRoom()

	type resp struct {
		RoomID string `json:"room_id"`
	}

	log.Println("Room created:", roomID)
	json.NewEncoder(w).Encode(resp{roomID})
}

// Handler for joining a WebRTC room
func JoinRoomRequestHandler(w http.ResponseWriter, r *http.Request) {
	roomID, ok := r.URL.Query()["roomID"]
	if !ok {
		http.Error(w, "Missing roomID", http.StatusBadRequest)
		return
	}

	// Upgrade HTTP connection to WebSocket
	ws, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Println("WebSocket Upgrade Error:", err)
		http.Error(w, "WebSocket upgrade failed", http.StatusInternalServerError)
		return
	}
	defer ws.Close()

	peerConnection, err := AllRooms.InsertIntoRoom(roomID[0], false, ws)
	if err != nil {
		log.Println("Error inserting into room:", err)
		return
	}
	defer peerConnection.Close()

	// Handle WebRTC signaling messages
	for {
		var msg map[string]interface{}
		err := ws.ReadJSON(&msg)
		if err != nil {
			log.Println("WebSocket Read Error:", err)
			break
		}

		// Process signaling messages
		switch msg["type"] {
		case "offer":
			handleOffer(peerConnection, ws, msg)
		case "iceCandidate":
			handleICECandidate(peerConnection, msg)
		default:
			fmt.Println("Unhandled message type:", msg["type"])
		}
	}

	// Clean up room after last participant leaves
	webrtcMutex.Lock()
	remainingParticipants := AllRooms.Get(roomID[0])
	if len(remainingParticipants) == 1 { // If last participant leaves, delete the room
		AllRooms.DeleteRoom(roomID[0])
		fmt.Println("Room Deleted:", roomID[0])
	}
	webrtcMutex.Unlock()
}

// Handles WebRTC offer and sends back an answer
func handleOffer(peerConnection *webrtc.PeerConnection, ws *websocket.Conn, msg map[string]interface{}) {
	webrtcMutex.Lock()
	defer webrtcMutex.Unlock()

	sdpString, ok := msg["sdp"].(string)
	if !ok {
		log.Println("Invalid SDP format")
		return
	}

	var offer webrtc.SessionDescription
	if err := json.Unmarshal([]byte(sdpString), &offer); err != nil {
		log.Println("Error unmarshaling offer:", err)
		return
	}

	if err := peerConnection.SetRemoteDescription(offer); err != nil {
		log.Println("Error setting remote description:", err)
		return
	}

	answer, err := peerConnection.CreateAnswer(nil)
	if err != nil {
		log.Println("Error creating answer:", err)
		return
	}

	if err := peerConnection.SetLocalDescription(answer); err != nil {
		log.Println("Error setting local description:", err)
		return
	}

	// Send answer back to the client
	answerMsg := map[string]interface{}{
		"type": "answer",
		"sdp":  answer,
	}
	if err := ws.WriteJSON(answerMsg); err != nil {
		log.Println("Error sending answer:", err)
	}
}

// Handles ICE candidate exchange
func handleICECandidate(peerConnection *webrtc.PeerConnection, msg map[string]interface{}) {
	webrtcMutex.Lock()
	defer webrtcMutex.Unlock()

	candidateString, ok := msg["candidate"].(string)
	if !ok {
		log.Println("Invalid ICE candidate format")
		return
	}

	var candidate webrtc.ICECandidateInit
	if err := json.Unmarshal([]byte(candidateString), &candidate); err != nil {
		log.Println("Error unmarshaling ICE candidate:", err)
		return
	}

	if err := peerConnection.AddICECandidate(candidate); err != nil {
		log.Println("Error adding ICE candidate:", err)
	}
}
