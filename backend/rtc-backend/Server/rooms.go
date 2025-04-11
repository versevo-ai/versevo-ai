package Server

import (
	"crypto/rand"
	"encoding/base64"
	"fmt"
	"log"
	"sync"

	"github.com/gorilla/websocket"
	"github.com/pion/webrtc/v3"
)

type Participant struct {
	Host           bool
	Conn           *websocket.Conn
	PeerConnection *webrtc.PeerConnection // Add PeerConnection
}

type RoomMap struct {
	Mutex sync.RWMutex
	Map   map[string][]Participant
}

func (r *RoomMap) Init() {
	r.Map = make(map[string][]Participant)
}

func (r *RoomMap) Get(roomID string) []Participant {
	r.Mutex.RLock()
	defer r.Mutex.RUnlock()
	return r.Map[roomID]
}

// func (r *RoomMap) CreateRoom() string {
// 	r.Mutex.Lock()
// 	defer r.Mutex.Unlock()
// 	rand.Seed(time.Now().UnixNano())
// 	var Letters = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
// 	b := make([]rune, 8)

// 	for i := range b {
// 		b[i] = Letters[rand.Intn(len(Letters))]
// 	}
// 	roomID := string(b)
// 	r.Map[roomID] = []Participant{}
// 	return roomID
// }

func (r *RoomMap) CreateRoom() (string, error) {
	r.Mutex.Lock()
	defer r.Mutex.Unlock()

	b := make([]byte, 12) // Generate 12 random bytes
	_, err := rand.Read(b)
	if err != nil {
		return "", fmt.Errorf("failed to generate random bytes: %w", err)
	}

	roomID := base64.RawURLEncoding.EncodeToString(b) // Encode to URL-safe base64
	r.Map[roomID] = []Participant{}
	return roomID, nil
}

func (r *RoomMap) InsertIntoRoom(roomID string, host bool, conn *websocket.Conn) (*webrtc.PeerConnection, error) { // Return PeerConnection
	r.Mutex.Lock()
	defer r.Mutex.Unlock()

	// Create Peer Connection
	peerConnection, err := createPeerConnection()
	if err != nil {
		return nil, err // Handle error
	}

	p := Participant{host, conn, peerConnection} // Store PeerConnection
	log.Println("Inserting into Room with RoomID: ", roomID)
	r.Map[roomID] = append(r.Map[roomID], p)
	return peerConnection, nil // Return the peer connection
}

func createPeerConnection() (*webrtc.PeerConnection, error) {

	// Define ICE servers
	iceServers := []webrtc.ICEServer{
		{
			URLs: []string{"stun:stun.l.google.com:19302"},
		},
	}

	// Create a new RTCPeerConnection
	config := webrtc.Configuration{
		ICEServers: iceServers,
	}

	peerConnection, err := webrtc.NewPeerConnection(config)
	if err != nil {
		return nil, err
	}

	// Handle ICE connection state changes
	peerConnection.OnICEConnectionStateChange(func(state webrtc.ICEConnectionState) {
		fmt.Printf("ICE Connection State has changed: %s\n", state.String())
	})

	return peerConnection, nil
}

func (r *RoomMap) DeleteRoom(roomID string) {
	r.Mutex.Lock()
	defer r.Mutex.Unlock()
	delete(r.Map, roomID)
}
