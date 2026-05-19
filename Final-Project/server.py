import http.server
import socketserver
import http.client
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
        if "json" in arguments:
            json_mode = True
        else:
            json_mode = False
        def read_html_file(filename):
            contents = Path("html/" + filename).read_text()
            contents = j.Template(contents)
            return contents
        content_type = "text/html"

        if path == "/" or path == "/index.html":
            self.send_response(200)
            contents = Path("html/index.html").read_text()

        elif path == "/listSpecies":
            self.send_response(200)

            SERVER = 'rest.ensembl.org'
            ENDPOINT = '/info/'
            PARAMS = f"species?content-type=application/json"
            conn = http.client.HTTPConnection(SERVER)
            conn.request("GET", ENDPOINT + PARAMS)
            response = conn.getresponse()
            data = json.loads(response.read().decode())
            species_lst = data["species"]

            if "limit" in arguments:
                limit = int(arguments["limit"][0])
            else:
                limit = None
            species = []
            total = len(species_lst)
            for i,s in enumerate(species_lst):
                if limit is None or i < limit:
                    species.append(s["common_name"])
            if json_mode:
                contents = json.dumps({"Species": species})
                content_type = "application/json"
            else:
                result = ""
                for i in species:
                    result += f"<li>{i}</li>"
                    contents = read_html_file("listspecies.html").render(total=total, limit=limit, species=result)
        elif path == "/karyotype":
            self.send_response(200)
            if "species" in arguments:
                species = arguments["species"][0]
                species = species.replace(" ", "%20").lower()
            else:
                species = None
            if not species:
                contents = Path("html/error.html").read_text()
            else:
                SERVER = "rest.ensembl.org"
                ENDPOINT = "/info/"
                PARAMS = f"assembly/{species}?content-type=application/json"
                conn = http.client.HTTPConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                if "karyotype" in data:
                    kar = data["karyotype"]
                else:
                    kar = []
                if json_mode:
                    contents = json.dumps({"Species": species, "Karyotype": kar})
                    content_type = "application/json"
                else:
                    result = "<p></p>".join(kar)
                    contents = read_html_file("karyotype.html").render(chromosome=result)
        elif path == "/chromosomeLength":
            self.send_response(200)
            if "species" in arguments:
                species = arguments["species"][0]
            else:
                species = None
            if "chromo" in arguments:
                chromosome = arguments["chromo"][0]
            else:
                chromosome = None
            if not species or not chromosome:
                contents = Path("html/error.html").read_text()
            else:
                SERVER = "rest.ensembl.org"
                ENDPOINT = '/info/'
                PARAMS = f"assembly/{species}?content-type=application/json"

                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                result = None
                if "top_level_region" in data:
                    top_level = data["top_level_region"]
                else:
                    top_level = []
                for region in top_level:
                    coord = region["coord_system"]
                    if coord == "chromosome":
                        chromo = region["name"]
                        if chromo == chromosome:
                            result = region["length"]
                if json_mode:
                    contents = json.dumps({"Species": species, "Chromosome": chromosome, "Length": result})
                    content_type = "application/json"
                else:
                    contents = read_html_file("chromosomeLength.html").render(length=result)
        elif path == "/geneLookup":
            self.send_response(200)
            if "gene" in arguments:
                gene = arguments["gene"][0]
            else:
                gene = None
            if not gene:
                contents = Path("html/error.html").read_text()
            else:
                SERVER = "rest.ensembl.org"
                ENDPOINT = f"/xrefs/symbol/homo_sapiens/{gene}?"
                PARAMS = "content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                stable_id = data[0]['id']
                if json_mode:
                    contents = json.dumps({"Gene": gene, "Stable_id": stable_id})
                    content_type = "application/json"
                else:
                    contents = read_html_file("geneLookup.html").render(gene=gene, stable_id=stable_id)
        elif path == "/geneSeq":
            self.send_response(200)
            if "gene" in arguments:
                gene = arguments["gene"][0]
            else:
                gene = None
            if not gene:
                contents = Path("html/error.html").read_text()
            else:
                SERVER = "rest.ensembl.org"
                ENDPOINT = f"/xrefs/symbol/homo_sapiens/{gene}?"
                PARAMS = "content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                stable_id = data[0]['id']

                ENDPOINT2 = "/sequence/id/"
                PARAMS2 = f"{stable_id}?content-type=application/json"
                conn.request("GET", ENDPOINT2 + PARAMS2)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                seq = data['seq']
                if json_mode:
                    contents = json.dumps({"Gene": gene, "Sequence": seq})
                    content_type = "application/json"
                else:
                    contents = read_html_file("geneSeq.html").render(gene=gene, seq=seq)
        elif path == "/geneInfo":
            self.send_response(200)
            if "gene" in arguments:
                gene = arguments["gene"][0]
            else:
                gene = None
            if not gene:
                contents = Path("html/error.html").read_text()
            else:
                SERVER = "rest.ensembl.org"
                ENDPOINT = f"/xrefs/symbol/homo_sapiens/{gene}?"
                PARAMS = "content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                stable_id = data[0]['id']

                ENDPOINT2 =  f"/lookup/id/{stable_id}?"
                PARAMS2 = "content-type=application/json"
                conn.request("GET", ENDPOINT2 + PARAMS2)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                start = data['start']
                end = data['end']
                length = end - start
                name = data['seq_region_name']

                if json_mode:
                    contents = json.dumps({"Gene": gene, "Start": start, "End": end, "Length": length, "Id": stable_id,
                                           "chromosome": name})
                    content_type = "application/json"
                else:
                    contents = read_html_file("geneInfo.html").render(gene=gene, start=start,
                    end=end, length=length, id=stable_id, name=name)
        elif path == "/geneCalc":
            self.send_response(200)
            if "gene" in arguments:
                gene = arguments["gene"][0]
            else:
                gene = None
            if not gene:
                contents = Path("html/error.html").read_text()
            else:
                SERVER = "rest.ensembl.org"
                ENDPOINT = f"/xrefs/symbol/homo_sapiens/{gene}?"
                PARAMS = "content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                stable_id = data[0]['id']

                ENDPOINT2 = "/sequence/id/"
                PARAMS2 = f"{stable_id}?content-type=application/json"
                conn.request("GET", ENDPOINT2 + PARAMS2)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                seq = data['seq']
                def count_base(seq, base):
                    return round(seq.count(base) / len(seq) * 100, 1)
                a = count_base(seq, "A")
                c = count_base(seq, "C")
                g = count_base(seq, "G")
                t = count_base(seq, "T")
                length = len(seq)
                if json_mode:
                    contents = json.dumps({"Gene": gene, "Length": length, "A": a, "C": c, "G": g, "T": t})
                    content_type = "application/json"
                else:
                    contents = read_html_file("geneCalc.html").render(gene=gene, length=length, a=a, c=c, g=g, t=t)
        elif path == "/geneList":
            self.send_response(200)
            if "chromo" in arguments:
                chromo = arguments["chromo"][0]
            else:
                chromo = None
            if "start" in arguments:
                start = arguments["start"][0]
            else:
                start = None
            if "end" in arguments:
                end = arguments["end"][0]
            else:
                end = None
            if not chromo or not start or not end:
                contents = Path("html/error.html").read_text()
            else:
                SERVER = "rest.ensembl.org"
                region = f"{chromo}:{start}-{end}"
                ENDPOINT = f"/overlap/region/homo_sapiens/{region}?"
                PARAMS = "feature=gene;content-type=application/json"
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                genes = []
                for item in data:
                    genes.append(item.get('external_name'))

                if json_mode:
                    contents = json.dumps({"Chromosome": chromo, "Start": start, "End": end, "Gene": genes})
                    content_type = "application/json"
                else:
                    contents = read_html_file("geneList.html").render(chromo=chromo, names=genes)
        else:
            self.send_response(404)
            contents = Path("html/error.html").read_text()
        self.send_header('Content-Type', content_type)
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


