class Seq:
    def __init__(self, bases=None):
        if bases is None:
            self.bases = "NULL"
            print("NULL sequence created")
            return
        valid_bases = "ACGT"
        for base in bases:
            if base not in valid_bases:
                self.bases = "ERROR"
                print("INVALID sequence!")
                return
        self.bases = bases
        print("New sequence created!")

    def __str__(self):
        return self.bases

    def __len__(self):
        if self.bases in ["NULL", "ERROR"]:
            return 0
        return len(self.bases)

    def count_base(self, base):
        if self.bases in ["NULL", "ERROR"]:
            return 0
        return self.bases.count(base)

    def count(self):
        bases = ["A", "C", "T", "G"]
        d = {}
        for base in bases:
            d[base] = self.bases.count(base)
        return d

    def reverse(self):
        if self.bases == "ERROR":
            return "ERROR"
        if self.bases == "NULL":
            return "NULL"
        return self.bases[::-1]

    def complement(self):
        if self.bases == "ERROR":
            return "ERROR"
        if self.bases == "NULL":
            return "NULL"
        complement_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
        complement_seq = ""
        for base in self.bases:
            complement_seq += complement_dict[base]
        return complement_seq

