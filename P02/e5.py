from Client0 import Client
from P01.Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.86"
PORT = 8081

c = Client(IP, PORT)

s = Seq()
s.read_fasta("sequences/FRAT1.txt")
seq = str(s)
print(f"Gene FRAT1: {seq}")

c.talk("Sending the FRAT1 Gene to the server, in fragment of 10 bases")
i = 0
while i < 5:
    print(f"fragment {i+1}: {seq[i * 10: (i + 1) * 10]}")
    c.talk(f"fragment {i+1}: {seq[i * 10: (i + 1) * 10]}")
    i += 1 