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
PARAMS = f"{genes["MIR633"]}??type=genomic;content-type=text/x-fasta"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)
response = conn.getresponse()
resp = response.read().decode()
print(f"Response received!: {response.status} {response.reason}\n")
print(f"Gene: {"MIR633"}")
print(f"Description: {resp.split(" ")[1].split("\n")[0]}")
print(f"Bases: {resp.split(" ")[1].split("\n")[1]}")





