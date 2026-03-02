from Seq1 import Seq

print("-----| Practice 1, Exercise 3 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print("")
lst = [s1, s2, s3]
n = 1
for seq in lst:
    print("Sequence", n, ":", seq)
    n += 1