def fibosum(n):
    seq = []
    a = 0
    b = 1
    seq.append(a)
    seq.append(b)
    for i in range(2, n):
        new = a + b
        seq.append(new)
        a = b
        b = new

    result = sum(seq)
    return result

print("Sum of the 5 first index:", fibosum(5))
print("Sum of the 10 first index:", fibosum(10))