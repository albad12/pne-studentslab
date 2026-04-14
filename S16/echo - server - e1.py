import http.server
import socketserver
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        from urllib.parse import parse_qs, urlparse
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)
        print(arguments)
        if path == "/" or path == "/echo" or arguments == "{}" :
            contents = Path("html/form - 1.html").read_text()
        elif path == "/echo":
            contents = Path("html/form-e1.html").read_text().replace("msg", arguments["msg"][0])
        else:
            contents = Path("html/error.html").read_text()
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