import http.server
import socketserver
from importlib.resources import contents
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path
        print(path)
        arguments = parse_qs(url_path.query)
        print(arguments)
        def read_html_file(filename):
            contents = Path("html/" + filename).read_text()
            contents = j.Template(contents)
            return contents
        sequences = ["ATTGCTGATGTAAG",
                     "TGCTGATGTCGATGT",
                     "CGTCGTGATGATGATCGT",
                     "ATCTGTCGTAGTAGT",
                     "ATGTCGTAGTGTGTATG"]
        U5 = Path
        ADA = Path
        FRAT1 = Path
        RNU6_269P = Path
        FXN = Path
        if path == "/":
           self.send_response(200)
           contents = Path("html/index.html").read_text()
        elif path == "/ping":
            self.send_response(200)
            contents = Path("html/ping.html").read_text()
        elif path == "/get":
            if "n" in arguments:
                n = int(arguments["n"][0])
                if 0 <= n <= 4:
                    seq = sequences[n]
            self.send_response(200)
            contents =
        elif path == "/gene":
            if "name" and "sequence" in arguments:
                name = arguments["name"][0]
                sequence = arguments["sequence"[0]
                for key, value in items():
                    if key = name
        else:
            self.send_response(404)
            contents = Path("html/error.html").read_text()

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