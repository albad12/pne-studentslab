from pathlib import Path

file_name = "Sequences/U5_sequence.fa"
content_2 = Path(file_name).read_text()

content_2_new = content_2.split("\n")

print("Body of the", file_name, "file:\n", "".join(content_2_new[1::]))