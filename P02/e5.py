from Client0 import Client
from Seq1 import Seq

practice = 2
exercise = 5
print(f"-----| Practice {practice}, Exercise {exercise} |------")

ip = "212.128.255.75"
port = 8080
c = Client(ip, port)
s = Seq()
frat = "Sequences/FRAT1_sequence.fa"
seq = s.read_fasta(frat)


for fragment in seq:
    n = 0
    while n < 5:
        lst = []
        for base in fragment:
            if len(lst) <= 10:
                lst.append(base)
        frg = ''.join(lst)
        n += 1
        print(f"Fragment {n}: {frg}")








