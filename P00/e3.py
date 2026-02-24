from Seq0 import *

u5 = seq_read_fasta("Sequences/U5_sequence.fa")
ada = seq_read_fasta("Sequences/ADA_sequence.fa")
frat = seq_read_fasta("Sequences/FRAT1_sequence.fa")
fxn = seq_read_fasta("Sequences/FXN_sequence.fa")

print("-----| Exercise 3 |------")

lst = [u5, ada, frat, fxn]
for sequence in lst:
    print("Gene -> Length:", seq_len(sequence))