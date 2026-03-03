def count_bases(seq):
    bases = {"A": 0, "C": 0, "T": 0, "G": 0}
    for base in seq:
        if base in bases:
            bases[base] += 1
    return bases
if __name__ == "__main__":
    seq = input("Introduce the sequence: ").upper()
    print("Total length:", len(seq))
    result = count_bases(seq)
    for base, count in bases.items():
        print(f'{base}: {count}')


def seq_count(seq):
    a = 0
    c = 0
    g = 0
    t = 0
    for i in seq:
        if i == "A":
            a += 1
        elif i == "C":
            c += 1
        elif i == "G":
            g += 1
        elif i == "T":
            t += 1
    return a, c, g, t

seq = input("Introduce the sequence: ").upper()
dna_len = len(seq)

a, c, g, t = seq_count(seq)

print("Total length:", dna_len)
print("A:", a)
print("C:", c)
print("G:", g)
print("T:", t)

#other way
print("____________other way (WITH FILES)_____________")
#other way

seq = input("Introduce the sequence: ").upper()
print("Total length:", len(seq))
bases = {"A": 0, "C": 0, "T": 0, "G": 0}
for base in seq:
    if base in bases:
        bases[base] += 1
for base, count in bases.items():
    print(f'{base}: {count}')