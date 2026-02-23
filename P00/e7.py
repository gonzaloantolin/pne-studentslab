from Seq0 import*

gene = "U5"
filename = "sequences/U5.txt"
sequence = seq_read_fasta(filename)

fragment = sequence[:20]
complement = seq_complement(fragment)

print(f"Gene {gene}")
print("Frag: ", fragment)
print("Comp: ", complement)