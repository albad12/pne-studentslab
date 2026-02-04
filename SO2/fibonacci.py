seq = []
a = 0
b = 1
seq.append(a)
seq.append(b)
for i in range(2, 11):
    new = a + b
    seq.append(new)
    a = b
    b = new

print("Fibonacci sequence with the first 11 elements:",seq)




