from pathlib import Path
filename = "Sequences/269P_sequence.fa"
file_contents = Path(filename).read_text()
print(file_contents)