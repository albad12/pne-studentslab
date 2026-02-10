lst = ["AGTACACTGGT", "ACCAGTGTACT","ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]

total = 0
a = 0
g = 0
c = 0
t = 0
for sequence in lst:
    total += len(sequence)
    for base in sequence:
        if base == "A":
            a += 1
        elif base == "G":
            g += 1
        elif base == "C":
            c += 1
        elif base == "T":
            t += 1

print("Total number of bases:",total)
print("A:", a)
print("G:", g)
print("C:", c)
print("T:", t)



f = open("dna.txt.", "r")
# Here we put the code
lines = f.readlines()
f.close()
print("From file:", lines)

for sequence in lines:
    sequence = sequence.strip() #removes spaces and newline characters at the end of the string

with open("dna.txt.", "r") as f:
    lines = f.readlines()        #one we process the line and go outside we don't need to call the close function



#from dna_count import count_bases
#if __name__ == "__main__":
    # main()