import json
import termcolor
from pathlib import Path

jsonstring = Path("people-1.json").read_text()
person = json.loads(jsonstring)

firstname = person['Firstname']
lastname = person['Lastname']
age = person['age']

print()
termcolor.cprint("Name: ", 'green', end="")
print(firstname, lastname)
termcolor.cprint("Age: ", "green", end="")
print(age)
