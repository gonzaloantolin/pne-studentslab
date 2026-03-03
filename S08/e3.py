import socket
# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.64" # depends on the computer the server is running
while True:
    message = input("Enter your message: ") # -- Ask the user for the message
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # -- Create the socket
    s.connect((IP, PORT)) # -- Establish the connection to the Server
    s.send(str.encode(message)) # -- Send the user message
    s.close()
