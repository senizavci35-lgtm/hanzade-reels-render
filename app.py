from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length)

        paket = json.loads(data)

        print("RENDER PAKETI:")
        print(paket)

        cevap = {
            "durum": "RENDER MOTORU AKTIF",
            "dosya": paket.get("ciktiAdi")
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(cevap).encode())


server = HTTPServer(("0.0.0.0", 8080), Handler)

print("HANZADE REELS RENDER CALISIYOR")

server.serve_forever()
