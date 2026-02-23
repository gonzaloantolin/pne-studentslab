from Seq0 import *

gene = "U5"
filename = "sequences/U5.txt"

sequence = seq_read_fasta(filename)

print("DNA file:", gene)
print("The first 20 bases are:")
print(sequence[:20])

