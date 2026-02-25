from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print("Sequence 1: (Length:", s1.len(), ")", s1, "\n", s1.count_dict(), "\n", s1.reverse() )
print("Sequence 2: (Length:", s2.len(), ")", s2, "\n", s2.count_dict(), "\n", s2.reverse() )