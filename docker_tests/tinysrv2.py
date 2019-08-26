import os
import http.server
import socketserver

PORT = int(os.getenv('TINYPORT',8100))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()