import http.server
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        if path == "/":
            self.send_response(200)
            contents = Path("html/form-e2.html").read_text()
        elif path == "/echo":
            self.send_response(200)
            body = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>Message Received</title>
            </head>
            <body>
                <h1>Message Received</h1>
            """
            if "msg" in arguments:
                message = arguments["msg"][0]
                if "upper" in arguments:
                    message = message.upper()
                body += f"<p>{message}</p>"
            else:
                body += "<p>No message received</p>"
            body += """
                <br>
                <a href="/">Main page</a>
            </body>
            </html>
            """
            contents = body
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