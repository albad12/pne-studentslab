from Seq0 import *

sequence = seq_read_fasta("Sequences/U5_sequence.fa")
print(sequence)
print(seq_fragment(sequence, 20))