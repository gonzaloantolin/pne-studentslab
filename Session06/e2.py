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
print(print_seqs(seq_list))


