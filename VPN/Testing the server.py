import socket

# Client-side parameters
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 443
BUFFER_SIZE = 16384

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = (SERVER_HOST, SERVER_PORT)
sock.connect(server_address)

# Send a message to the server
message = 'Hello, server!'
sock.send(message.encode())

# Receive the server's response
response = sock.recv(BUFFER_SIZE)
print('Server response:', response.decode())

# Close the socket
sock.close()