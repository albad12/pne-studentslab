from Seq0 import *

u5 = seq_read_fasta("Sequences/U5_sequence.fa")
ada = seq_read_fasta("Sequences/ADA_sequence.fa")
frat = seq_read_fasta("Sequences/FRAT1_sequence.fa")
fxn = seq_read_fasta("Sequences/FXN_sequence.fa")

sequences = [("U5",u5), ("ADA",ada), ("FRAT", frat), ("FXN",fxn)]
print("-----| Exercise 5 |------")
for name,seq in sequences:
    print("Gene", name, ":",seq_count(seq))

