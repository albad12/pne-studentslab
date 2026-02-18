from Seq0 import *

u5 = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/U5_sequence.fa")
ada = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/ADA_sequence.fa")
frat = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/FRAT1_sequence.fa")
fxn = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/FXN_sequence.fa")

lst = [u5, ada, frat, fxn]
for seq in lst:
    print(seq_count(seq))

