from Seq0 import *

u5 = seq_read_fasta("Sequences/U5_sequence.fa")
u5_comp = seq_complement(u5)

print("-----| Exercise 7 |------")
print(seq_fragment(u5,20))
print(seq_fragment(u5_comp, 20))

