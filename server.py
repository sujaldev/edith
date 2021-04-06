from config_reader import Config
import socket

# Get Config File
config = Config().config
HOST = config["HOST"]
PORT = int(config["PORT"])

print(f"Locally hosted on http://{'localhost' if HOST == '127.0.0.1' else HOST}:{PORT}")

# Create Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)


while True:
    client_s, address = s.accept()
    data = client_s.recv(1024).decode()
    print(data)
    html = """\
HTTP/1.1 200 OK

<h1>Test</h1>
"""
    client_s.send(bytes(html, "utf-8"))
    client_s.close()
