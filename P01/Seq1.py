# __init__(self, strbases = None) is initial default(by default is None       s = Seq() => s = Seq(None)
# s = Seq("ATCG")

class Seq:
    def __init__(self, strbases = None):
        self.strbases = strbases
        lst = ["A", "T", "C", "G"]
        if strbases == None:
            self.strbases = "NULL"
            print("NULL sequence created")
        else:
            for letter in strbases:
                if letter not in lst:
                    strbases = "ERROR"
                elif letter in lst:
                    strbases = strbases

            if strbases == "ERROR":
                print("INVALID sequence!")
            else:
                print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL":
            result = 0
        elif self.strbases == "ERROR":
            result = 0
        else:
            result = len(self.strbases)
        return result

    def count(self, base):
        count = 0
        if self.strbases == "NULL":
            count = 0
        elif self.strbases == "ERROR":
            count = 0
        else:
            for a in self.strbases:
                if a == base:
                    count += 1
        return count

    def count_dict(self):
        d = {"A": 0, "T": 0, "G": 0, "C": 0}
        for base in self.strbases:
            if base in d:
                d[base] += 1
        return d

    def reverse(self):
        lst = []
        if self.strbases == "NULL":
            new_seq = self.strbases
        elif self.strbases == "ERROR":
            new_seq = self.strbases
        else:
            seq_r = self.strbases[::-1]
            for base in seq_r:
                lst.append(base)
            new_seq = ''.join(lst)
        return new_seq

    def complement(self):
        bases = {"A": "T", "T": "A", "G": "C", "C": "G"}
        seq = []
        if self.strbases == "NULL":
            new_seq = self.strbases
        elif self.strbases == "ERROR":
            new_seq = self.strbases
        else:
            for base in self.strbases:
                if base in bases:
                    seq.append(bases[base])
                new_seq = ''.join(seq)
        return new_seq

    def seq_read_fasta(self, filename):

        content = Path(filename).read_text()
        content_new = content.split("\n")
        result = ("".join(content_new[1::]))
        return result