from pathlib import Path

file = "Sequences/ADA_sequence.fa"
content_1 = Path(file).read_text()
content_1 = content_1.split("\n")
content_1 = content_1[1::]
gene = "".join(content_1)

file2 = "Sequences/ADA_EXONS.txt"
exon_text = Path(file2).read_text()

exons = []
current = ""
for line in exon_text.splitlines():
    if line.startswith(">"):
        if current:
            exons.append(current)
            current = ""
    else:
        current += line.strip()
if current:
    exons.append(current)



max_coord = 44652852
print("Exon | Length | Start | End")
print("-------------------------------------------------")

exon_number = 1
for exon in exons:
    index = gene.find(exon)
    length = len(exon)

    start = max_coord - index
    end = max_coord - (index + length - 1)
    if start > end:
        start, end = end, start
    print(exon_number, "|", length, "|", start, "|", end)
    exon_number += 1




