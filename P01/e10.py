from Seq1 import Seq

seqs = {"U5": "Sequences/U5_sequence.fa",
        "ADA": "Sequences/ADA_sequence.fa",
        "FRAT": "Sequences/FRAT1_sequence.fa",
        "FXN": "Sequences/FXN_sequence.fa",
        "RNU6_269P": "Sequences/269P_sequence.fa"}

for name, seq in seqs.items():
    s = Seq()
    s.read_fasta(seq)
    value = s.seq_count()
    max_count = 0
    max_base = ""

    for base,n in value.items():
        if n > max_count:
            max_count = n
            max_base = base

    print("Sequence", name, ": Most frequent Base:", max_base)
