from Seq0 import *

u5 = seq_read_fasta("Sequences/U5_sequence.fa")
ada = seq_read_fasta("Sequences/ADA_sequence.fa")
frat = seq_read_fasta("Sequences/FRAT1_sequence.fa")
fxn = seq_read_fasta("Sequences/FXN_sequence.fa")

sequences = [("U5",u5), ("ADA",ada), ("FRAT", frat), ("FXN",fxn)]
for name,seq in sequences:
    value = seq_count(seq)
    max_count = 0
    max_base = ""
    for base,n in value.items():
        if n > max_count:
            max_count = n
            max_base = base

    print("Gene", name, ":Most frequent base:", max_base, "(value:", max_count,")")