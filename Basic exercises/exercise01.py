dna = "ATGCGATCGATCGATCGATCGA"
print("The total length of the sequence is:", len(dna))
print("The first 5 elements are:", dna[0:5])
print("The last 3 characters are:", dna[-3:])
print("The sequence in lowercase:", dna.lower())
print("The times the substring ATC appears is:", dna.count("ATC"))
print("The ARN would be", dna.replace("T", "U"))
