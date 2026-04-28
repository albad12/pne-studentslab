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
        contents = ""
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        def read_html_file(filename):
            contents = Path("html/" + filename).read_text()
            contents = j.Template(contents)
            return contents

        if path == "/":
           self.send_response(200)
           contents = Path("index.html").read_text()
        elif path == "/listspecies":
            self.send_response(200)
            SERVER = 'rest.ensembl.org'
            ENDPOINT = '/info/'
            PARAMS = f"species?content-type=application/json"
            # conditon for if lim or not but this is the code
            conn = http.client.HTTPSConnection(SERVER)
            conn.request("GET", ENDPOINT + PARAMS)
            response = conn.getresponse()
            data = json.loads(response.read().decode())
            print(f"Response received!: {response.status} {response.reason}\n")
            specie = data["species"]
            for i, dictspecies in enumerate(specie):
                print(dictspecies["display_name"])
        elif path == "karyotype":
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
        elif path == "/chromosomeLength":
            pass
        else:
            self.send_respone(404)
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