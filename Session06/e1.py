class Seq:
    def __init__(self, bases: str):
        valid_bases = "ACGT"
        for base in bases:
            if base not in valid_bases:
                self.bases = "ERROR"
                print("INCORRECT Sequence detected")
                return
        self.bases = bases
        print("New sequence created!")
    def __str__(self):
        return self.bases

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
