import http. client
import json
specie = input(str("Enter the species name: "))
SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/'
PARAMS = f"assembly/{specie}?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)
response = conn.getresponse()
data = json.loads(response.read().decode())
print(f"Response received!: {response.status} {response.reason}\n")
print(data["karyotype"])

