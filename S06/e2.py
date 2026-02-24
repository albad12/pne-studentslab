class Seq:
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
    def len(self):
        return len(self.strbases)

    def print_seqs(self):
        result = ("Sequence", seq_list.index(self.strbases), ": (Length:", seq.len(), ") ", self.strbases)
        return result

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
for seq in seq_list:
    print(print_seqs())