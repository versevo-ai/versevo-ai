import ssl
import pathlib
from websockets.sync.client import connect

# Create SSL context for client
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_verify_locations(localhost_pem)

URI = "wss://localhost:8765/dj/send"
try:
    with connect(uri=URI, ssl=ssl_context, server_hostname="localhost") as websocket:
        websocket.send("Hii From Client at /dj/send")
        response = websocket.recv()
        print(f"server: {response}")
except Exception as e:
    print(f"Error: {e}")



URI = "wss://localhost:8765/dj/rv"
try:
    with connect(uri=URI, ssl=ssl_context, server_hostname="localhost") as websocket:
        websocket.send("Hii From Client at /dj/rv")
        response = websocket.recv()
        print(f"server: {response}")
except Exception as e:
    print(f"Error: {e}")