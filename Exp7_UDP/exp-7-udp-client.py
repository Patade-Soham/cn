import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ("127.0.0.1", 5000)

client.sendto(b"START", server)

with open("test.txt", "rb") as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client.sendto(data, server)

client.sendto(b"END", server)

print("File sent successfully.")
client.close()
