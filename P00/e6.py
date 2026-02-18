from Seq0 import *

u5 = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/U5_sequence.fa")
lst = []
for base in u5:
    if len(lst) < 20:
        lst.append(base)

seq = ''.join(lst)
print(seq)
print(seq_reverse(seq, 20))
