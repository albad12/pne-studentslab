from Seq0 import *

u5 = seq_read_fasta("Sequences/U5_sequence.fa")
ada = seq_read_fasta("Sequences/ADA_sequence.fa")
frat = seq_read_fasta("Sequences/FRAT1_sequence.fa")
fxn = seq_read_fasta("Sequences/FXN_sequence.fa")

lst = [u5, ada, frat, fxn]
print("-----| Exercise 5 |------")
for seq in lst:
    print(seq_count(seq))

