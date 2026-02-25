from Seq1 import Seq
s0 = Seq()
s1 = Seq("ACTGA")
s2 = Seq("Invalid sequence")

print(f"Sequence 1: (Length {len(s0)}) {s0}")
print("A:", s0.count_base("A"), ", C:",  s0.count_base("C"), ", G:", s0.count_base("G"), ", T", s0.count_base("T"))
print(f"Sequence 1: (Length {len(s1)}) {s1}")
print("A:", s1.count_base("A"), ", C:",  s1.count_base("C"), ", G:", s1.count_base("G"), ", T", s1.count_base("T"))
print(f"Sequence 1: (Length {len(s2)}) {s2}")
print("A:", s2.count_base("A"), ", C:",  s2.count_base("C"), ", G:", s2.count_base("G"), ", T", s2.count_base("T"))