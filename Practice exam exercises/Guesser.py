import random


class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []
    def __str__(self):
        return f"{self.secret_number}, {self.attempts}"
    def guess(self, number):
        number = int(number)
        if number == self.secret_number:
            return f"You won after {len(self.attempts)} attempts"
        elif number > self.secret_number:
            self.attempts.append(number)
            return f"Lower"
        else:
            self.attempts.append(number)
            return f"Higher"





