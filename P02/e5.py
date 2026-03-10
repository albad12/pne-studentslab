from Client0 import Client
from Seq1 import Seq


practice = 2
exercise = 5
print(f"-----| Practice {practice}, Exercise {exercise} |------")

ip = "127.0.0.1"
port = 8080
c = Client(ip, port)
s = Seq()
frat = "Sequences/FRAT1_sequence.fa"
seq = s.read_fasta(frat)

print(f"Gene FRAT1:{s}")

seq = str(s)
message = ("Sending FRAT1 Gene to the server, in fragments of 10 bases...")
c.talk(message)

for i in range(5):
    fragment = seq[i * 10:(i + 1) * 10]
    print(f" Fragment {i + 1}: {fragment}")
    c.talk(f"Fragment {i + 1}: {fragment}")







