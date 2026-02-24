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

    def generate_seqs(pattern, number):
        lst = []
        for i in range(1, number + 1):
            lst.append(Seq(pattern * i))
        return lst

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
