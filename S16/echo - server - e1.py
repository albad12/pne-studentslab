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
        if path == "/":
            contents = Path("html/form - 1.html").read_text()
        elif path == "/echo":
            body = """
              <!DOCTYPE html>
              <html lang="en" dir="ltr">
                <head>
                  <meta charset="utf-8">
                  <title>Message Received</title>
                </head>
                <body>
                  <h1>Message Received</h1>
        """
       for key, value in arguments:
           if key == "msg":
               body += f"""
                    <p>{value[0]}</p>
                    <p><p>
                    <a href="http://127.0.0.1:8080/">Main Page</a>

    """
        contents = "\n" + body
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