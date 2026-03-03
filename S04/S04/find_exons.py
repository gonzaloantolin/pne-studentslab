from pathlib import Path
file_path = Path("sequences/ADA.txt")
gene_content = file_path.read_text().split("\n")

gene_lines = gene_content[1:]
gene_sequence = ""

for line in gene_lines:
    gene_sequence += line

exon_file = Path("sequences/ADA_EXONS.txt")
exon_content = exon_file.read_text().split('\n')

exons = []
current_exon = ""

for line in exon_content:
    if line.startswith(">"):
        if current_exon != "":
            exons.append(current_exon)
            current_exon = ""
    else:
        current_exon += line
if current_exon != "":
    exons.append(current_exon)

chromosome_max = 44652852

for i in range(len(exons)):

    exon = exons[i]
    i = gene_sequence.find(exon)

    length = len(exon)

    start = chromosome_max - i
    end = chromosome_max - (i + length - 1)

    print("Exon", i+1)
    print("Length:", length)
    print("Start:", start)
    print("End:", end)
    print("----------------------")



