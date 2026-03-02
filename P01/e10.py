from Seq1 import Seq

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gene in genes:
    s = Seq()
    s.read_fasta(f"sequences/{gene}.txt")
    bases_dict = s.count()
    most_frequent = max(bases_dict, key=bases_dict.get)
    print(f"Gene {gene}: Most frequent Base: {most_frequent}")