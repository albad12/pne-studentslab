import http.server
import http.client
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import json

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        def read_html_file(filename):
            contents = Path("html/" + filename).read_text()
            contents = j.Template(contents)
            return contents
        if path == "/":
           self.send_response(200)
           contents = Path("html/index.html").read_text()
        elif path == "/listspecies":
            self.send_response(200)
            SERVER = 'rest.ensembl.org'
            ENDPOINT = '/info/'
            PARAMS = f"species?content-type=application/json"
            conn = http.client.HTTPSConnection(SERVER)
            conn.request("GET", ENDPOINT + PARAMS)
            response = conn.getresponse()
            data = json.loads(response.read().decode())
            species_list = data["species"]
            limit = arguments.get("limit", [None])[0]
            if limit:
                limit = int(limit)
            species = []
            count = 0
            for specie in species_list:
                if limit is None or count < limit:
                    species.append(specie["common_name"])
                    count += 1

            result = "\n".join(species)
            contents = read_html_file("species.html").render(total=count, limit=limit, species=result)
        elif path == "karyotype":
            self.send_response(200)
            specie = input(str("Enter the species name: "))
            SERVER = 'rest.ensembl.org'
            ENDPOINT = '/info/'
            PARAMS = f"assembly/{specie}?content-type=application/json"

            conn = http.client.HTTPSConnection(SERVER)
            conn.request("GET", ENDPOINT + PARAMS)
            response = conn.getresponse()
            data = json.loads(response.read().decode())
            print(f"Response received!: {response.status} {response.reason}\n")
            kar = data["karyotype"]
            kart = []
            for i in kar:
                kart.append(i)
            result = "\n".join(kart)
            contents = read_html_file("karyotype.html").render(chromosomes=result)
        elif path == "/chromosomeLength":
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
                        result = region["length"]
            contents = read_html_file("chromosome.html").render(length=result)
        else:
            self.send_response(404)
            contents = Path("error/html")

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        self.end_headers()
        self.wfile.write(contents.encode())


Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()