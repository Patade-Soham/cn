import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 5000))

print("Waiting for file...")

data, client = server.recvfrom(1024)

with open("received.txt", "wb") as file:
    while True:
        data, client = server.recvfrom(1024)
        if data == b"END":
            break
        file.write(data)

print("File received successfully.")
server.close()
