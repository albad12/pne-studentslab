import json
import termcolor
from pathlib import Path

jsonstring = Path("people-e1.json").read_text()
person = json.loads(jsonstring)
people = person["people"]

print()
for i, dictperson in enumerate(people):
    termcolor.cprint("Name: ", 'green', end="")
    print(dictperson['Firstname'], dictperson['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(dictperson['age'])

    phoneNumbers = dictperson["phoneNumber"]
    termcolor.cprint("Phone numbers: ", 'green', end="")
    print(len(phoneNumbers))

    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint(" Phone " + str(i + 1) + ":", 'blue')
        termcolor.cprint("\t - Type: ", 'red', end="")
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])

