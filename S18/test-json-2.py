import json
import termcolor
from pathlib import Path

jsonstring = Path("people-2.json").read_text()
person = json.loads(jsonstring)

print()
termcolor.cprint("Name: ", 'green', end="")
print(person["Firstname"], person["Lastname"])
termcolor.cprint("Age: ", 'green', end="")
print(person["age"])

phoneNumbers = person["phoneNumber"]
termcolor.cprint("Phone numbers: ", 'green', end="")
print(len(phoneNumbers))

for i, num in enumerate(phoneNumbers):
    termcolor.cprint("Phone" + str(i) + ":", 'blue', end="")
    print(num)
