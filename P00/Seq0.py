from pathlib import Path

def seq_ping():
    print("Ok")

def seq_read_fasta(filename):
    content = Path(filename).read_text()
    content_new = content.split("\n")
    result = ("".join(content_new[1::]))
    return result

def seq_len(seq):
    result = len(seq)
    return result

def seq_count_base(seq, base):
    count = 0
    for a in seq:
        if a == base:
            count += 1
    return count

def seq_count(seq):
    d = {"A": 0, "T":0, "G": 0, "C": 0}
    d["A"] = seq_count_base(seq,"A")
    d["T"] = seq_count_base(seq,"T")
    d["G"] = seq_count_base(seq, "G")
    d["C"] = seq_count_base(seq,"C")
    return d

def seq_reverse(seq, n):
    lst = []
    seq_r = seq[::-1]
    for base in seq_r:
        if len(lst) < n :
            lst.append(base)

    new_seq = ''.join(lst)
    return new_seq

def seq_complement(seq):
    bases = {"A": "T", "T": "A", "G": "C", "C": "G" }
    new_seq = []
    for base in seq:
        if base in bases:
           new_seq.append(bases[base])
    return new_seq

def seq_fragment(seq,n):
    lst = []
    for base in seq:
        if len(lst) < n:
            lst.append(base)
    seq = ''.join(lst)
    return seq

