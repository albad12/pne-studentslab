import http.server
import socketserver
import termcolor
from pathlib import Path


PORT = 8081

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.requestline.split(" ")[1]
        file = path.replace("/", "")
        if path == "/" :
            contents = Path("index.html").read_text()
        else:
            try:
                contents = Path(file).read_text()
            except FileNotFoundError:
                contents = Path("error.html").read_text()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())
        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()