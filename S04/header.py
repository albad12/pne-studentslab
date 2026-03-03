from pathlib import Path
file_name = "Sequences/269P_sequence.fa"
content = Path(file_name).read_text()


content_new = content.split("\n")

print("First line of the", file_name, "file:\n",content_new[0])