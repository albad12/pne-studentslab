def grades(grade):
    if 10 >= grade >= 9:
        result = "A"
    elif 8.9 >= grade >= 7:
        result = "B"
    elif 6.9 >= grade >= 5:
        result = "C"
    elif 4.9 >= grade >= 3:
        result = "D"
    elif 2.9 >= grade >= 0:
        result = "F"
    else:
        result ="Not valid"
    return result

grade = float(input("Enter your grade: "))
print("Score:", grade, "->", grades(grade))