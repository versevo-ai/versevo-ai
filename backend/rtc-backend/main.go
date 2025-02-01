package main

import (
	"fmt"
	"github.com/versevo-ai/backend/rtc-backend/Server"
	"log"
	"net/http"
)

func main() {
	Server.AllRooms.Init()
	http.HandleFunc("/create", Server.CreateRoomRequestHandler)
	http.HandleFunc("/join", Server.JoinRoomRequestHandler)
	log.Println("Starting Server on Port 8000")
	fmt.Println("  ")
	err := http.ListenAndServe(":8000", nil)
	if err != nil {
		log.Fatal(err)
	}
}
