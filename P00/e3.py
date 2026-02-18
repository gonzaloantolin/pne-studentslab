from Seq0 import *
genes = ["U5", "ADA", "FRAT1", "FXN"]

for gene in genes:
    filename = f"sequences/{gene}.txt"
    sequence = seq_read_fasta(filename)
    length = seq_len(sequence)
    print(f"Gene {gene} -> Length: {length}")
