def total_bases(dna_list):
    a = c = g = t = 0
    for seq in dna_list:
        for base in seq:
            if base == "A":
                a += 1
            elif base == "C":
                c += 1
            elif base == "G":
                g += 1
            elif base == "T":
                t += 1
    return a + c + g + t

def different_bases(dna_list):
    a = c = g = t = 0
    for seq in dna_list:
        for base in seq:
            if base == "A":
                a += 1
            elif base == "C":
                c += 1
            elif base == "G":
                g += 1
            elif base == "T":
                t += 1
    return a, c, g, t

dna_list = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]
a, c, g, t = different_bases(dna_list)
print("The total number of bases is:", total_bases(dna_list))
print("A:", a)
print("C:", c)
print("G:", g)
print("T:", t)

#other way
print("____________other way (WITH FILES)_____________")
#other way

#lines = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]
#print("from variable:", lines)
from dna_count import count_bases
f = open("dna.txt.", "r") #one way of opening files
#code goes here
lines = f.readlines()
f.close()

with open("dna.txt.", "r") as f: #another way of opening files (this ones better)
    lines = f.readlines()

total_number = 0
bases = {"A": 0, "C": 0, "T": 0, "G": 0}

for seq in lines:
    seq = seq.strip() #remove spaces and newline characters at the end of the string
    total_number += len(seq)
    result = count_bases(seq)
    for key in result:
        bases[key] += result[key]


print("Total number of bases:", total_number)

for base, count in bases.items():
    print(f'{base}: {count}')


#from dna_count import count_bases
#if __name__ == "__main__":