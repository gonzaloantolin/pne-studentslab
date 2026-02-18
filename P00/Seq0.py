from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    lines = file_contents.split("\n")
    sequence = ""
    for line in lines:
        if not line.startswith(">"):
            sequence += line.strip()
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    bases = ["A", "C", "T", "G"]
    d = {}
    for base in bases:
        d[base] = seq.count(base)
    return d

def seq_reverse(seq, n):




