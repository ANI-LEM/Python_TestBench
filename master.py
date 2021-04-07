import time
import socket
import sys
import os

# Initialize s to socket
s = socket.socket()

# Initialize the host
host = "LTF-ANI2"

# Initiaze the port
port = 5000

# bind the socket with port and host
s.connect((host, port))

print("Connected to Server.")

# recieve the command from master program
command = s.recv(1024)
command = command.decode()

# match the command and execute it on slave system
if command == "open":
    print("Command is :", command)
    s.send("Command recieved".encode())

    # you can give batch file as input here
    os.system('ls')