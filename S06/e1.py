class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        lst = ["A", "T", "C", "G"]
        for letter in strbases:
            if letter not in lst:
                strbases = "ERROR"
            else:
                strbases = strbases
        if strbases == "ERROR":
            print("ERROR")
        else:
            print("New sequence created!")

    def __str__(self):
        lst = ["A", "T", "C", "G"]
        for letter in self.strbases:
            if letter not in lst:
                self.strbases = "ERROR"
            else:
                self.strbases = self.strbases
        return self.strbases



s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")



