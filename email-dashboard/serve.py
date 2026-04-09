import http.server
import os
import socketserver

os.chdir(os.path.dirname(os.path.abspath(__file__)))
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 8090), handler) as httpd:
    print("Serving on port 8090")
    httpd.serve_forever()
