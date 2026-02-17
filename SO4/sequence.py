from pathlib import Path

file_name = "Sequences/ADA_sequence.fa"
content_3 = Path(file_name).read_text()

content_3 = content_3.split("\n")
content_3 = content_3[1::]
content_3_new = "".join(content_3)

print(len(content_3_new))