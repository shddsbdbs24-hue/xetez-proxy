import os
from http.server import SimpleHTTPRequestHandler
import socketserver

class ProxyXetez(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Xetez Proxy Server Activo en Estados Unidos</h1>")

PORT = int(os.environ.get("PORT", 8080))

with socketserver.TCPServer(("", PORT), ProxyXetez) as httpd:
    print(f"Servidor XETEZ corriendo")
    httpd.serve_forever()
