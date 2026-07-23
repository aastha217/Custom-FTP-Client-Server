# Custom FTP Client-Server

A custom File Transfer Protocol (FTP) application built using Python socket programming. The system follows a client-server architecture and allows authenticated users to upload, download, list, and delete files on a centralized server while supporting multiple concurrent client connections through multithreading.

---

## Features

- User authentication
- File upload
- File download
- Directory listing
- File deletion
- Multi-client support
- Concurrent connections using multithreading
- Server activity logging
- TCP-based communication

---

## Technologies Used

- Python
- TCP Sockets
- Multithreading
- File Handling
- Logging Module

---

## Concepts Demonstrated

- Computer Networks
- TCP/IP Communication
- Socket Programming
- Client-Server Architecture
- Concurrency and Threading
- File System Operations

---

## Project Structure

```text
FTP_Project/
│
├── client/
│   └── client.py
│
├── server/
│   ├── server.py
│   └── server.log
│
├── storage/
│
├── downloads/
│
└── users.txt
```

---

## Supported Commands

| Command | Description |
|---------|-------------|
| `LOGIN username password` | Authenticate user |
| `LIST` | Display files on the server |
| `UPLOAD filename` | Upload a file to the server |
| `DOWNLOAD filename` | Download a file from the server |
| `DELETE filename` | Delete a file from the server |
| `QUIT` | Disconnect from the server |

---

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd FTP_Project
```

### 2. Start the Server

```bash
cd server
python server.py
```

### 3. Start the Client

Open a new terminal and run:

```bash
cd client
python client.py
```

---

## Sample Session

```text
Username: admin
Password: 1234

LOGIN SUCCESS

FTP> LIST
notes.txt
report.pdf

FTP> UPLOAD test.txt
UPLOAD SUCCESS

FTP> DOWNLOAD notes.txt
DOWNLOAD SUCCESS

FTP> DELETE test.txt
DELETE SUCCESS

FTP> QUIT
Goodbye
```

---

## Logging

Server activities are recorded in `server.log`, including:

- Client connections
- Login attempts
- File uploads
- File downloads
- File deletions
- Client disconnections

---

## Future Enhancements

- Password hashing
- SSL/TLS encryption
- GUI using Tkinter
- Database-based authentication
- User roles and permissions

---

## Key Learning Outcomes

- Implemented TCP-based client-server communication using sockets.
- Developed a custom application-layer protocol for file transfer.
- Managed concurrent client connections using multithreading.
- Applied authentication and file system operations in a networked environment.
- Gained practical experience in designing and testing distributed systems.

---
