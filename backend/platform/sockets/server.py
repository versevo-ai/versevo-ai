from websockets.sync.server import *
import ssl
import pathlib
# from client import Client

# Create SSL context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

def handler(websocket:ServerConnection):
    try:
        stream = websocket.recv()
        print(f"Client : {stream}")
        websocket.send("Thank You ,from Server",text=True)
    except Exception as e:
        print(f"Error Occured : {e}")

def main():
    try:
        # Start the server
        with serve(handler=handler, host="localhost", port=8765, ssl_context=ssl_context) as server:
            print("WebSocket server running on wss://localhost:8765")
            server.serve_forever()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
