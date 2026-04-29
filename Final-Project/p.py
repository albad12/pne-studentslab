import http. client
import json

specie = input(str("Enter the species name: "))
SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/'
PARAMS = f"assembly/{specie}?content-type=application/json"

conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)
response = conn.getresponse()
data = json.loads(response.read().decode())
chromosome = str(input("Enter the chromosome: "))
top_level = data["top_level_region"]
for i, region in enumerate(top_level):
    coord = region["coord_system"]
    if coord == "chromosome":
        chromo = region["name"]
        if chromo == chromosome:
            print(f"{region["length"]}")