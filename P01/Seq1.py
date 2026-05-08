from pathlib import Path
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

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        file_contents = file_contents.split("\n")
        body = "".join(file_contents[1:])
        self.bases = body
        return self.bases

    def composition(self):
        total = len(self)
        A = self.count_base("A")
        C = self.count_base("C")
        G = self.count_base("G")
        T = self.count_base("T")

        pa = round(((A / total) * 100), 2)
        pc = round(((C / total) * 100), 2)
        pg = round(((G / total) * 100), 2)
        pt = round(((T / total) * 100), 2)

        return {
            "A": {
                "total A bases": A,
                "%": pa
            },
            "C": {
                "total C bases": C,
                "%": pc
            },
            "G": {
                "total G bases": G,
                "%": pg
            },
            "T": {
                "total T bases": T,
                "%": pt
            }
        }

