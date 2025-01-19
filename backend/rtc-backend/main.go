package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/websocket"
)

const Port = ":8080"

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

func main() {

	http.HandleFunc("/ws", handleWebsocket)
	fs := http.FileServer(http.Dir("./web"))
	http.Handle("/", fs)

	fmt.Printf("Starting Server at - http://localhost%s/n", Port)
	log.Fatal(http.ListenAndServe(Port, nil))

}

func handleWebsocket(w http.ResponseWriter, r *http.Request) {

	conn, err := upgrader.Upgrade(w, r, nill)
	if err != nil {
		log.Println(err)
	}

	defer conn.Close()

}
