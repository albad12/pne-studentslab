def summ(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res

print("The total sum of the 20 first integers is:", summ(20))
print("The total sum of the 100 first integers is:", summ(100))