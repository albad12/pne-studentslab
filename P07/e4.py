import http. client

genes = {"FRAT": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"
         }

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
gene = str(input("Write the gene name: "))
PARAMS = f"{genes[gene]}?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)
response = conn.getresponse()
resp = response.read().decode()
print(f"Response received!: {response.status} {response.reason}\n")

print(f"Gene: {gene}")
print(f"Description: {resp.split(" ")[1].split("\n")[0]}")
print(f"New sequence created!")
seq = resp.split(" ")[1].split("\n")[1]
length = len(seq)
def bases (base):
    count = 0
    for b in seq:
        if b == base:
            count += 1
            return round((count / length), 2) * 100
result = (
        f" Total length: {length}\n"
        f" A: {bases('A')}%\n "
        f"C: {bases('C')}%\n "
        f"G: {bases('G')}%\n "
        f"T: {bases('T')}%\n"
    )
