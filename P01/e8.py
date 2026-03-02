from Seq1 import Seq

print("-----| Practice 1, Exercise 8 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

lst = [s1, s2, s3]
n = 1
for seq in lst:
    print("Sequence", n, ": (Length:", seq.len(), ")", seq, "\n", seq.count_dict(), "\n", seq.reverse(), "\n", seq.complement())
