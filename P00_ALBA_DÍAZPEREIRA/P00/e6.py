from Seq0 import *

u5 = seq_read_fasta("Sequences/U5_sequence.fa")
seq  = seq_fragment(u5, 20)
print("------| Exercise 6 |------")
print("Fragment:",seq)
print("Reversed fragment:",seq_reverse(seq, 20))
