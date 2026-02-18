from Seq0 import seq_read_fasta
from Seq0 import seq_count_base

u5 = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/U5_sequence.fa")
ada = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/ADA_sequence.fa")
frat = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/FRAT1_sequence.fa")
fxn = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/FXN_sequence.fa")
bases = ["A", "T", "G", "C"]
lst = [u5, ada, frat, fxn]
print("------ | Exercise 4 |------")
for seq in lst:
    for base in bases:
        print(base, ":",seq_count_base(seq, base))


#sequences = [u5, ada, frat, fxn]
#for sequence in sequences:
    #print(sequence)
    #for base in bases:
        #print(base, ":",seq_count_base(sequences, base))
