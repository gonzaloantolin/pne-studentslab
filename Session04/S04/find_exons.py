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

print(current_exon)
