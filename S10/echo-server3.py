import socket
import termcolor

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1" # the IP address depends on the machine running the server

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

i = 1
clients = []

while True and len(clients) <= 5:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print(f"CONNECTION {i}, Client IP, PORT: ('{client_ip_port[0]}', {client_ip_port[1]}) ")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        termcolor.cprint(f"Message received: {msg}", "green" )

        # -- Send a response message to the client
        response = f"ECHO: {msg}\n"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()

    if len(clients) == 5:
        j = 0
        for client in clients:
            print(f"Client: {j}: {client}")
            j += 1
    else:
        i += 1