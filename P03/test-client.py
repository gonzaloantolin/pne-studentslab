from P02.Client0 import Client

IP = "127.0.0.1"
PORT = 8080

def main():
    c = Client(IP, PORT)
    print("------| Practice 3, Exercise 7 |-------")
    print(c)

    print("Testing PING...")
    print(c.talk("PING").strip())

    print("Testing GET...")
    seq0 = c.talk("GET 0").strip()
    print(f"GET 0: {seq0}")

    for i in range(1, 5):
        res = c.talk(f"GET {i}").strip()
        print(f"GET {i}: {res}")

    print("Testing INFO...")
    print(f"Sequence: {seq0}")
    print(c.talk(f"INFO {seq0}").strip())

    print("Testing COMP...")
    print(f"COMP {seq0}")
    print(c.talk(f"COMP {seq0}").strip())

    print("Testing REV...")
    print(f"REV {seq0}")
    print(c.talk(f"REV {seq0}").strip())

    print("Testing GENE...")
    genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
    for gene in genes:
        full_response = c.talk(f"GENE {gene}").strip()
        print(f"GENE {gene}")
        print(full_response)

if __name__ == "__main__":
    main()