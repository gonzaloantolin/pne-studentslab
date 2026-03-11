from P02.Client0 import Client

IP = "127.0.0.1"
PORT = 8080

print("-----| Practice 3, Exercise 7 |------")
print(f"Connection to SERVER at {IP}, PORT: {PORT}")

c = Client(IP, PORT)

# ----------------
# PING
# ----------------
print("* Testing PING...")
response = c.talk("PING")
print(response)

# ----------------
# GET
# ----------------
print("\n* Testing GET...")

seq0 = ""

for i in range(5):
    command = f"GET {i}"
    response = c.talk(command)
    print(f"{command}: {response.strip()}")

    if i == 0:
        seq0 = response.strip()

# ----------------
# INFO
# ----------------
print("\n* Testing INFO...")
response = c.talk(f"INFO {seq0}")
print(response)

# ----------------
# COMP
# ----------------
print("* Testing COMP...")
print(f"COMP {seq0}")
response = c.talk(f"COMP {seq0}")
print(response)

# ----------------
# REV
# ----------------
print("* Testing REV...")
print(f"REV {seq0}")
response = c.talk(f"REV {seq0}")
print(response)

# ----------------
# GENE
# ----------------
print("* Testing GENE...")

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gene in genes:
    print(f"GENE {gene}")
    response = c.talk(f"GENE {gene}")
    print(response)