from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")

s = Seq()
s.read_fasta("Sequences/U5_sequence.fa")
print("Sequence: (Length:", s.len(), ")", s, "\n Bases:", s.count_dict(), "\n Rev:", s.reverse(),
          "\n Comp:", s.complement())