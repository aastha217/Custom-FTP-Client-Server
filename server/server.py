import socket
import os

HOST = "127.0.0.1"
PORT = 5000


def authenticate(username, password):
    with open("../users.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(":")

            if username == u and password == p:
                return True

    return False


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print("Server Started...")
print("Waiting for connections...")

while True:

    client_socket, addr = server.accept()

    print(f"Connected: {addr}")

    while True:

        command = client_socket.recv(1024).decode()

        if not command:
            break

        print("Received:", command)

        parts = command.split()

        if parts[0] == "LOGIN":

            username = parts[1]
            password = parts[2]

            if authenticate(username, password):
                client_socket.send("LOGIN SUCCESS".encode())
            else:
                client_socket.send("LOGIN FAILED".encode())

        elif parts[0] == "LIST":

            files = os.listdir("../storage")

            response = "\n".join(files)

            client_socket.send(response.encode())

        elif parts[0] == "UPLOAD":

            filename = parts[1]
            filesize = int(parts[2])

            filepath = f"../storage/{filename}"

            with open(filepath, "wb") as f:

                received = 0

                while received < filesize:

                    data = client_socket.recv(1024)

                    f.write(data)

                    received += len(data)

            client_socket.send("UPLOAD SUCCESS".encode())

        elif parts[0] == "QUIT":

            client_socket.send("Goodbye".encode())
            break

    client_socket.close()