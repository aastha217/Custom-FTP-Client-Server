import socket
import os
import threading

HOST = "127.0.0.1"
PORT = 5000


def authenticate(username, password):
    with open("../users.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(":")

            if username == u and password == p:
                return True

    return False


def handle_client(client_socket, addr):

    print(f"Connected: {addr}")

    while True:

        try:
            command = client_socket.recv(1024).decode()

            if not command:
                break

            print(f"[{addr}] {command}")

            parts = command.split()

            if len(parts) == 0:
                continue

            if parts[0] == "LOGIN":

                username = parts[1]
                password = parts[2]

                if authenticate(username, password):
                    client_socket.send(
                        "LOGIN SUCCESS".encode()
                    )
                else:
                    client_socket.send(
                        "LOGIN FAILED".encode()
                    )

            elif parts[0] == "LIST":

                files = os.listdir("../storage")

                if len(files) == 0:
                    response = "Storage is empty"
                else:
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

                client_socket.send(
                    "UPLOAD SUCCESS".encode()
                )

            elif parts[0] == "DOWNLOAD":

                filename = parts[1]

                filepath = f"../storage/{filename}"

                if not os.path.exists(filepath):

                    client_socket.send(
                        "FILE_NOT_FOUND".encode()
                    )

                else:

                    filesize = os.path.getsize(filepath)

                    client_socket.send(
                        f"SIZE {filesize}".encode()
                    )

                    with open(filepath, "rb") as f:

                        while True:

                            chunk = f.read(1024)

                            if not chunk:
                                break

                            client_socket.sendall(chunk)

            elif parts[0] == "DELETE":

                filename = parts[1]

                filepath = f"../storage/{filename}"

                if os.path.exists(filepath):

                    os.remove(filepath)

                    client_socket.send(
                        "DELETE SUCCESS".encode()
                    )

                else:

                    client_socket.send(
                        "FILE NOT FOUND".encode()
                    )

            elif parts[0] == "QUIT":

                client_socket.send("Goodbye".encode())
                break

            else:

                client_socket.send(
                    "INVALID COMMAND".encode()
                )

        except Exception as e:

            print(f"Error with {addr}: {e}")
            break

    client_socket.close()

    print(f"Disconnected: {addr}")


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

server.bind((HOST, PORT))
server.listen()

print("Server Started...")
print("Waiting for connections...")

while True:

    client_socket, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, addr)
    )

    thread.start()