import random
import termcolor

class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []
    def __str__(self):
        return self.secret_number, self.attempts
    def guess(self, number):
        if int(number) == self.secret_number:
            termcolor.cprint(f"You won after {len(self.attempts)} attempts", "green")
        elif int(number) < self.secret_number:
            self.attempts.append(number)
            termcolor.cprint(f"Lower", "blue")
        else:
            self.attempts.append(number)
            termcolor.cprint(f"Higher", "yellow")





