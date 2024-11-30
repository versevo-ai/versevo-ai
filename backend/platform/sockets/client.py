from websockets.sync.client import connect

def client(msg="Hello"):
    URI = "wss://localhost:8765/"
    try:
        with connect(URI) as websocket:
            websocket.send(msg)
            response = websocket.recv()
            print(f"Received from server: {response}")
    except Exception as e:
        print(f"Error: {e}")