def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

text = "  Hello, World! Welcome to Python Programming.  "
text= text.strip()
print("Stripped:", text)
print("Word count:",count_words(text))
print("Title case:", text.title())
print("Starts with Hello:", text.startswith("Hello"))
print("Ends with ing.:", text.endswith("ing."))
print("Python position:", text.find("Python"))
text_2 = text.split()
text_3 = "-".join(text_2)
print("Joined:", text_3)