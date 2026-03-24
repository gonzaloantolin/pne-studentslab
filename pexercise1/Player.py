import socket

IP = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

print("Connected to the game!")
print("Guess a number between 1 and 100")

playing = True
while playing:
    number = input("Enter your guess: ")

    if number.isdigit():
        client.send(number.encode())

        response = client.recv(2048).decode()
        print("Server:", response)

        if "won" in response:
            print("Game finished!")
            client.close()
            playing = False
    else:
        print("Invalid number")
