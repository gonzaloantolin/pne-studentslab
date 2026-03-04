from Client0 import Client
from P01.Seq1 import Seq

U5 = "sequences/U5.txt"
ADA = "sequences/ADA.txt"
FRAT1 = "sequences/FRAT1.txt"

s = Seq()
s2 = Seq()
s3 = Seq()

gene = {"U5": U5, "ADA": ADA, "FRAT1": FRAT1}

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.86"
PORT = 8081

c = Client(IP, PORT)
for genes, gene_2 in gene.items():
    print(f"Sending {genes} to the server")
    response = c.talk(s.read_fasta(gene_2))
    print(f"Response: {response}")


