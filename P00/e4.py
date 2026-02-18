from Seq0 import *

genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "T", "G"]

for gene in genes:
    filename = f"sequences/{gene}.txt"
    sequence = seq_read_fasta(filename)
    print(f"Gene {gene}:")
    for base in bases:
        count = seq_count_base(sequence, base)
        print(f"  {base}: {count}")

