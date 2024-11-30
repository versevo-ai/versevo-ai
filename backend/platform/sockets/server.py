from websockets.sync.server import serve
import ssl
import pathlib
from client import client

# Create SSL context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

def echo():
    for messge in client():
        print(messge)

def main():
    try:
        # Start the server
        with serve(echo, "localhost", 8765, ssl_context=ssl_context) as server:
            print("WebSocket server running on wss://localhost:8765")
            server.serve_forever()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
