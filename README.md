# Custom FTP Client-Server

A custom File Transfer Protocol (FTP) application built using Python socket programming. The system follows a client-server architecture and allows authenticated users to upload, download, list, and delete files on a centralized server while supporting multiple concurrent client connections through multithreading.

## Features

* User authentication
* File upload
* File download
* Directory listing
* File deletion
* Multi-client support
* Concurrent connections using multithreading
* Server activity logging
* TCP-based communication

## Technologies Used

* Python
* TCP Sockets
* Multithreading
* File Handling
* Logging Module

## Concepts Demonstrated

* Computer Networks
* TCP/IP Communication
* Socket Programming
* Client-Server Architecture
* Concurrency and Threading
* File System Operations

## Project Structure


FTP_Project
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


## Supported Commands

| Command                 | Description               |
| ----------------------- | ------------------------- |
| LOGIN username password | Authenticate user         |
| LIST                    | Display files on server   |
| UPLOAD filename         | Upload file to server     |
| DOWNLOAD filename       | Download file from server |
| DELETE filename         | Delete file from server   |
| QUIT                    | Disconnect from server    |

## Setup

### Start the Server


cd server
python server.py


### Start the Client


cd client
python client.py


## Sample Session


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


## Logging

Server activities are recorded in `server.log`, including:

* Client connections
* Login attempts
* File uploads
* File downloads
* File deletions
* Client disconnections

## Future Enhancements

* Password hashing
* SSL/TLS encryption
* GUI using Tkinter
* Database-based authentication
* User roles and permissions


## Key Learning Outcomes

* Implemented TCP-based client-server communication using sockets.
* Developed a custom application-layer protocol for file transfer.
* Managed concurrent client connections using multithreading.
* Applied authentication and file system operations in a networked environment.
* Gained practical experience in designing and testing distributed systems.

