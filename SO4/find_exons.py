from pathlib import Path

file = "Sequences/ADA_sequence.fa"
content_1 = Path(file).read_text()
content_1 = content_1.split("\n")
content_1 = content_1[1::]
content_1_new = "".join(content_1)

file2 = "Sequences/ADA_EXONS.txt"
content_2 = Path(file2).read_text()
content_2 = content_2.split("\n")
content_2 = content_2[1::]
content_2_new = "".join(content_2)



