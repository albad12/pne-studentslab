import json
import http.client

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/'
PARAMS = f"species?content-type=application/json"
conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)
response = conn.getresponse()
data = json.loads(response.read().decode())
species_list = data["species"]

species = []
count = 0
limit = int(input("Enter the limit: "))
for specie in species_list:
    if count < limit:
        species.append(specie["common_name"])
        count += 1

result = "\n".join(species)
print(result)