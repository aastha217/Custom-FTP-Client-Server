import socket
import os

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

client.connect((HOST, PORT))

username = input("Username: ")
password = input("Password: ")

login_command = f"LOGIN {username} {password}"

client.send(login_command.encode())

response = client.recv(1024).decode()

print(response)

if response == "LOGIN SUCCESS":

    while True:

        command = input("FTP> ")

        parts = command.split()

        if len(parts) == 0:
            continue

        if parts[0].upper() == "UPLOAD":

            filename = parts[1]

            try:

                with open(filename, "rb") as f:

                    data = f.read()

                filesize = len(data)

                client.send(
                    f"UPLOAD {filename} {filesize}".encode()
                )

                client.sendall(data)

                response = client.recv(1024).decode()

                print(response)

            except FileNotFoundError:

                print("File not found")

        elif parts[0].upper() == "DOWNLOAD":

            filename = parts[1]

            client.send(command.encode())

            response = client.recv(1024).decode()

            if response == "FILE_NOT_FOUND":

                print("File not found on server")

            else:

                filesize = int(
                    response.split()[1]
                )

                filepath = f"../downloads/{filename}"

                with open(filepath, "wb") as f:

                    received = 0

                    while received < filesize:

                        data = client.recv(1024)

                        f.write(data)

                        received += len(data)

                print("DOWNLOAD SUCCESS")

        else:

            client.send(command.encode())

            response = client.recv(4096).decode()

            print(response)

        if command.upper() == "QUIT":
            break

client.close()