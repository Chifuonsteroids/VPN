import socket
import threading

# Server-side parameters
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 443

# Size of receive buffer
BUFFER_SIZE = 16384

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = (SERVER_HOST, SERVER_PORT)
sock.bind(server_address)

# Set the socket to listen for incoming connections
sock.listen(1  )

# Function to handle incoming client connections
def handle_client_connection(client_socket):
  request = client_socket.recv(BUFFER_SIZE)
  # Do something with the request here
  response = 'OK\n'
  client_socket.send(response)
  client_socket.close()

while True:
  # Wait for a client connection
  print('Waiting for a client connection...')
  client_sock, client_addr = sock.accept()
  print('Client connected:', client_addr)
  # Start a new thread to handle the client connection
  client_thread = threading.Thread(
    target=handle_client_connection,
    args=(client_sock,)  # without comma you'd get a...
  )
  client_thread.start()
