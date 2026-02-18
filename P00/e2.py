from Seq0 import *

filename = "sequences/U5.txt"

sequence = seq_read_fasta(filename)

print("DNA file:", filename)
print("The first 20 bases are:")
print(sequence[:20])

