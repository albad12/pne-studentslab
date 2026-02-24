from Seq0 import *

u5 = seq_read_fasta("Sequences/U5_sequence.fa")
ada = seq_read_fasta("Sequences/ADA_sequence.fa")
frat = seq_read_fasta("Sequences/FRAT1_sequence.fa")
fxn = seq_read_fasta("Sequences/FXN_sequence.fa")

print("-----| Exercise 3 |------")

sequences = [("U5",u5), ("ADA",ada), ("FRAT", frat), ("FXN",fxn)]
for name,seq in sequences:
    print("Gene", name, "-> Length:", seq_len(seq))