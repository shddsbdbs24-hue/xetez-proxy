import os
import http.server
import urllib.request

class ProxyRealXetez(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Captura la URL que pide tu navegador XETEZ
        url = self.path
        if url.startswith("/"):
            # Si entras directo al server, muestra un estado limpio
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Xetez Tunnel Activo y Listo")
            return

        try:
            # Descarga la pagina real desde EE.UU.
            req = urllib.request.Request(url, headers=dict(self.headers))
            with urllib.request.urlopen(req) as response:
                self.send_response(response.status)
                for header, value in response.getheaders():
                    self.send_header(header, value)
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            self.send_error(500, f"Error en el tunel: {e}")

PORT = int(os.environ.get("PORT", 8080))
server = http.server.ThreadingHTTPServer(("", PORT), ProxyRealXetez)
print(f"Tunel Xetez corriendo en puerto {PORT}")
server.serve_forever()
