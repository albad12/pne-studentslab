import http.server
import socketserver

# Handler is the name given to the object that is called when a
# client connects and needs to be attended.
# In this example we are using the Handler provided by the http.server module
PORT = 8081

socketserver.TCPServer.allow_reuse_address = True
#defines the behaviour the server will have whenever it is asked something
Handler = http.server.SimpleHTTPRequestHandler
#Simple behaviour: read, find the file, send the file to the client
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    # ------ Main Loop: attend theclient. Whenevr there is a new
    # ------ client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped!")
        httpd.server_close()


