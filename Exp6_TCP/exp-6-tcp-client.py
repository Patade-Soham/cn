import socket

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
server_ip = input("Enter Server IP Address: ")
client.connect((server_ip, 5000))

# Send message
# message = input("Enter message for server: ")
message = "Hello server"
client.send(message.encode())

# Receive reply
reply = client.recv(1024).decode()
print("Server:", reply)

# Close connection
client.close()
