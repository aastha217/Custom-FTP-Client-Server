import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Server Started...")

client_socket, addr = server.accept()

print("Connected:", addr)

msg = client_socket.recv(1024).decode()

print("Client:", msg)

client_socket.send("Hello Client".encode())

client_socket.close()