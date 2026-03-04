from Client0 import Client
from P01.Seq1 import Seq
FRAT1 = "sequences/FRAT1.txt"
s = Seq()

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.86"
PORT = 8081
PORT2 = 8082

c1 = Client(IP, PORT)
c2 = Client(IP, PORT2)

def cut(string):
    fragments = []
    for i in range(10):
        start_index = i * 10
        end_index = start_index + 10
        fragment = string[start_index:end_index]
        fragments.append(fragment)
        return fragments
print(c1)
print(c2)
print(f"Sending the FRAT1 Gene to the server")
fragments = cut(s.read_fasta(FRAT1))
print(f"Gene FRAT1 : {s.read_fasta(FRAT1)}")
for index in range(len(fragments)):
    i = index + 1
    ch = fragments[index]

    print(f"fragment {i}: {ch}")
    if i % 2 != 0:
        response = c1.talk(ch)
    else:
        response = c2.talk(ch)
