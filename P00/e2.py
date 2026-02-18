from Seq0 import seq_read_fasta

sequence = seq_read_fasta("/home/alumnos/albadiaz/PycharmProjects/pne-studentslab/SO4/Sequences/U5_sequence.fa")
print(sequence)

lst = []
for base in sequence:
    if len(lst) < 20:
        lst.append(base)

seq = ''.join(lst)
print(seq)
