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


def print_seqs(seq_list):
    for seq in seq_list:
        print("Sequence", seq_list.index(seq), ": (Length:", seq.len(), ") ", seq)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)