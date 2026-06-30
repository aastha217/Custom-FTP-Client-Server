import socket

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

        if parts[0].upper() == "UPLOAD":

            filename = parts[1]

            with open(filename, "rb") as f:

                data = f.read()

            filesize = len(data)

            client.send(
                f"UPLOAD {filename} {filesize}".encode()
            )

            client.sendall(data)

            response = client.recv(1024).decode()

            print(response)

        else:

            client.send(command.encode())

            response = client.recv(4096).decode()

            print(response)

        if command.upper() == "QUIT":
            break

client.close()