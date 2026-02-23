from Seq0 import*

genes = ["U5", "ADA", "FRAT1", "FXN"]

for gene in genes:
    filename = f"sequences/{gene}.txt"

    sequence = seq_read_fasta(filename)
    counts = seq_count(sequence)
    most_frequent = max(counts, key=counts.get)
    print(f"Gene {gene}: Most frequent Base: {most_frequent}")