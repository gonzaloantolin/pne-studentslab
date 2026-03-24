import socket
import random
PORT = 8080
IP ="127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []
    def guess(self, number):
        self.attempts.append(number)
        if number == self.secret_number:
            return f"You won after {len(self.attempts)} attempts"
        elif number > self.secret_number:
            return "Lower"
        else:
            return "Higher"

while True:
    print("Game started!")
    print("Waiting for players...")

    try:
        cs, client_ip_port = ls.accept()

    except KeyboardInterrupt:
        print("Game stopped by player")
        ls.close()
        exit()

    else:
        print("A player has connected to the game!")

        game = NumberGuesser()

        while True:

            playing = True

            while playing:
                msg_raw = cs.recv(2048)

                if msg_raw:
                    try:
                        number = int(msg_raw.decode().strip())
                        response = game.guess(number)
                        cs.send(response.encode())

                        if "won" in response:
                            cs.close()
                            playing = False

                    except:
                        cs.send("Invalid input".encode())
                else:
                    playing = False
