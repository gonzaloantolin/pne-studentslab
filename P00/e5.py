from Seq0 import *
genes = ["U5", "ADA", "FRAT1", "FXN"]
for gene in genes:
    filename = f"sequences/{gene}.txt"
    seq = seq_read_fasta(filename)
    counts = seq_count(seq)
    print(f"Gene {gene}: {counts}")



