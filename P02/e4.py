from Client0 import Client
from Seq1 import Seq

practice = 2
exercise = 4
print(f"-----| Practice {practice}, Exercise {exercise} |------")

ip = "212.128.255.75"
port = 8080
c = Client(ip, port)
seqs = {"U5": "Sequences/U5_sequence.fa",
        "ADA": "Sequences/ADA_sequence.fa",
        "FRAT": "Sequences/FRAT1_sequence.fa"}

for name, seq in seqs.items():
    s = Seq()
    s.read_fasta(seq)
    response = c.talk(f"Sending {name} Gene to the server...")
    print(f"To Server: Sending {name} Gene to the server... ")
    print()
    print(f"From Server:\n {response}")
    response = c.talk(f"{s}")
    print(f"To server:{s}")
    print(f"From Server:\n {response}")

