from Seq1 import Seq

s = Seq()
s.read_fasta("sequences/U5.txt")

print(f"Sequence : (Length: {len(s)}) {s}")
print(f"  Bases: {s.count()}")
print(f"  Rev:   {s.reverse()}")
print(f"  Comp:  {s.complement()}")