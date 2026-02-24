from Seq0 import *

u5 = seq_read_fasta("Sequences/U5_sequence.fa")
ada = seq_read_fasta("Sequences/ADA_sequence.fa")
frat = seq_read_fasta("Sequences/FRAT1_sequence.fa")
fxn = seq_read_fasta("Sequences/FXN_sequence.fa")
bases = ["A", "T", "G", "C"]
lst = [u5, ada, frat, fxn]
print("-----| Exercise 4 |------")
for seq in lst:
    for base in bases:
        print(base, ":",seq_count_base(seq, base))


#sequences = [u5, ada, frat, fxn]
#for sequence in sequences:
    #print(sequence)
    #for base in bases:
        #print(base, ":",seq_count_base(sequences, base))
