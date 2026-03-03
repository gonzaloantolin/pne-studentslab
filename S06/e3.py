class Seq:
    def __init__(self, bases: str):
        valid_bases = "ACGT"
        for base in bases:
            if base not in valid_bases:
                self.bases = "ERROR"
                print("INCORRECT Sequence detected")
                return
        self.bases = bases
        print("New sequence created!") #podria quitarlo, se imprime xq se runeatodo el codigo y cmo la seq es correcta se nos imprime

    def __str__(self):
        return self.bases

def print_seqs(seq_list):
    for i in range(len(seq_list)):
        seq = seq_list[i]
        print(f"Sequence {i}: (Length: {len(seq.bases)}) {seq}")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]


def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number + 1):
        seq_list.append(Seq(pattern * i))
    return seq_list

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
