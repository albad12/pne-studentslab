def dna_bases_iterator(seq):
    seq = seq.upper()
    length = len(seq)
    a = 0
    t = 0
    c = 0
    g = 0
    for base in seq:
        if base == "A":
            a += 1
        elif base == "T":
            t += 1
        elif base == "C":
            c += 1
        elif base == "G":
            g += 1
    return length, a, t, g, c

seq = input("Enter the DNA sequence: ")
l, a, t, g, c = dna_bases_iterator(seq)

print("Total length:", l)
print("A:", a)
print("T:", t)
print("C:", c)
print("G:", g)

# bases = {"A": 0, "T": 0, "C":0, "G": 0}
# for base in sequence:
    # if base in bases:
        # bases[base] += 1

# for base, count, in bases.items():
    # print(f'{base}: {count}')