from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

bases = ["A", "T", "G", "C"]
print("Sequence 1: (Length:", s1.len(), ")", s1 )
for base in bases:
    print(base, ":", s1.count(base))
print("Sequence 2: (Length:", s2.len(), ")", s2 )
for base in bases:
    print(base, ":", s2.count(base))
print("Sequence 3: (Length:", s3.len(), ")", s3 )
for base in bases:
    print(base, ":", s3.count(base))
