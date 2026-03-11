from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

for i in range(5):
    message = f"Message {i}"

    print(f"To server: {message}")

    c = Client(IP, PORT)
    response = c.talk(message)

    print(f"From server: {response}")