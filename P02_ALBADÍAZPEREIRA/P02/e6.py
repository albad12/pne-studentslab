from Client0 import Client
from Seq1 import Seq

practice = 2
exercise = 6
print(f"-----| Practice {practice}, Exercise {exercise} |------")

ip = "212.128.255.75"
port1 = 8080
port2 = 8081
c1 = Client(ip, port1)
print(c1)
c2 = Client(ip, port2)
print(c2)
s = Seq()
frat = "Sequences/FRAT1_sequence.fa"
seq = s.read_fasta(frat)

print(f"Gene FRAT1:{s}")
message = ("Sending FRAT1 Gene to the server, in fragments of 10 bases...")
c1.talk(message)
c2.talk(message)

count = 1
for i in range(10):
    fragment = seq[i * 10:(i + 1) * 10]
    print(f" Fragment {count}: {fragment}")
    if count % 2 == 1:
        c1.talk(f" Fragment {count}: {fragment}")
    else:
        c2.talk(f" Fragment {count}: {fragment}")
    count += 1