from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

bases = ["A", "T", "G", "C"]
lst = [s1, s2, s3]
n = 1
for seq in lst:
    print("Sequence", n,": (Length:", seq.len(), ")", seq)
    for base in bases:
        print(base, ":", seq.count(base))
    n += 1