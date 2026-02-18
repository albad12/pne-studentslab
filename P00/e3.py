from Seq0 import seq_read_fasta
from Seq0 import seq_len

u5 = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/U5_sequence.fa")
ada = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/ADA_sequence.fa")
frat = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/FRAT1_sequence.fa")
fxn = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/FXN_sequence.fa")

print("------| Exercise 3 |------")

lst = [u5, ada, frat, fxn]
for sequence in lst:
    print("Gene -> Length:", seq_len(sequence))