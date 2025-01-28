package main

import (
  "encoding/json"
  "fmt"
  "github.com/gorilla/websocket"
  "github.com/pion/webrtc/v3"
  "log"
  "net/http"
)

// Define constants and variables
const (
  webPort = ":8080"
)

var upgrader = websocket.Upgrader{
  ReadBufferSize:  1024,
  WriteBufferSize: 1024,
}

func main() {
  // Setup HTTP server
  http.HandleFunc("/ws", handleWebSocket)
  fs := http.FileServer(http.Dir("./web"))
  http.Handle("/", fs)

  fmt.Printf("Starting server at http://localhost%s\n", webPort)
  log.Fatal(http.ListenAndServe(webPort, nil))
}

func createPeerConnection() (*webrtc.PeerConnection, error) {
  // Define ICE servers

  iceServers := []webrtc.ICEServer{
    {
      URLs: []string{"stun:stun.l.google.com:19305,stun:stun.l.google.com:19302"},
    },
  }

  // Create a new RTCPeerConnection
  config := webrtc.Configuration{
    ICEServers: iceServers,
  }
  peerConnection, err := webrtc.NewAPI().NewPeerConnection(config)
  if err != nil {
    panic(err)
  }

  // peerconnection close handling

  defer func() {
    if err := peerConnection.Close(); err != nil {
      fmt.Printf("Error closing peer connection: %s\n", err)
    }
  }()

  // Handle ICE connection state changes
  peerConnection.OnICEConnectionStateChange(func(state webrtc.ICEConnectionState) {
    fmt.Printf("ICE Connection State has changed: %s\n", state.String())
  })

  return peerConnection, nil
}

func handleWebSocket(w http.ResponseWriter, r *http.Request) {
  conn, err := upgrader.Upgrade(w, r, nil)
  if err != nil {
    log.Println(err)
    return
  }
  defer conn.Close()

  for {
    _, message, err := conn.ReadMessage()
    if err != nil {
      log.Println(err)
      break
    }

    var msg map[string]interface{}
    if err := json.Unmarshal(message, &msg); err != nil {
      log.Println(err)
      continue
    }

    switch msg["type"] {
    case "join":
      log.Printf("%s joined the session", msg["name"])
    case "offer":
      // Handle offer message
    case "answer":
      // Handle answer message
    case "candidate":
      // Handle ICE candidate message
    }
  }
}
