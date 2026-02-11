def is_even(n):
    if n % 2 == 0:
        result = "True"
    else:
        result = "False"
    return result

n = int(input("Enter the number: "))
print("is even", n, "=", is_even(n))

def classify_triangle(a, b, c):
    if a == b and b == c:
        result = "Equilateral"
    elif (a == b and b != c) or (b == c and a != b) or (a == c and a != b):
        result = "Isosceles"
    elif a != b and a != b and c != b :
        result = "Scalene"
    return result

a = int(input("Enter side: "))
b = int(input("Enter side: "))
c = int(input("Enter side: "))

print("classify triangle (a,b,c) = ", classify_triangle(a,b,c))
