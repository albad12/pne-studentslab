import http. client
import json

genes = {"FRAT1": "ENSG00000165879",
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
PARAMS = f"{genes["MIR633"]}?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)
response = conn.getresponse()
data = json.loads(response.read().decode())
print(f"Response received!: {response.status} {response.reason}\n")
print(data)

print(data['id'])
print(data['seq'])
seq = data['seq']
print(f"Total lenght: {len(seq)}")
def info(seq):
    print(f"Start: {seq[0]}")
    print(f"End: {seq[-1]}")
    print(f"Length:{len(seq)}")
    print(f"id: {data["id"]}")
info(seq)
def count(seq, base):
    count = 0
    for a in seq:
        if a == base:
            count += 1
    return f"{base}: {count} ({round((count / len(seq)) * 100, 1)})%"


print(f"{count(seq, "A")}\n"
        f"{count(seq, "C")}\n"
        f"{count(seq, "G")}\n"
        f"{count(seq, "T")}")

