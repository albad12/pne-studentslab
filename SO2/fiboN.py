# Description: Convert the previous program into the function fibon(n) that calculates the nth Fibonacci term and return it
# The main program should call the fibon() function and print the 5th, 10th and 15th terms in the console
#
# Execute the program step by step.
# Use the step into button for watching how the fibon() function works. Try also the step out button.
def fibon(n):
    seq = []
    a = 0
    b = 1
    seq.append(a)
    seq.append(b)
    for i in range(2,n):
        new = a + b
        seq.append(new)
        a = b
        b = new

    return seq[n - 1]

print("5th Fibonacci term:", fibon(5))
print("10th Fibonacci term:", fibon(10))
print("15th Fibonacci term:", fibon(15))