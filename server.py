#!/usr/bin/env python3
"""
Servidor com proxy para Bitaxe — resolve problemas de CORS.
Uso: python server.py
Dashboard: http://localhost:8080/dashboard.html
Proxy: http://localhost:8080/proxy/192.168.18.98/api/system/info
"""
import http.server
import urllib.request
import urllib.error
import sys
import os

PORT = 8080

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Proxy: /proxy/<ip>/<path> -> http://<ip>/<path>
        if self.path.startswith('/proxy/'):
            parts = self.path[7:].split('/', 1)
            if len(parts) == 2:
                ip, api_path = parts
                url = f"http://{ip}/{api_path}"
                try:
                    req = urllib.request.Request(url, headers={
                        'User-Agent': 'BitaxeDashboard/1.0'
                    })
                    with urllib.request.urlopen(req, timeout=5) as resp:
                        data = resp.read()
                        self.send_response(200)
                        self.send_header('Content-Type', 'application/json')
                        self.send_header('Access-Control-Allow-Origin', '*')
                        self.end_headers()
                        self.wfile.write(data)
                except Exception as e:
                    self.send_response(502)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(f'{{"error":"{str(e)}"}}'.encode())
                return
        # Normal static files
        super().do_GET()

    def log_message(self, format, *args):
        if '/proxy/' in str(args[0]):
            print(f"[PROXY] {args[0]}")
        else:
            pass  # silence static file logs

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Servidor rodando em http://localhost:{PORT}/dashboard.html")
    print(f"Proxy API:     http://localhost:{PORT}/proxy/192.168.18.98/api/system/info")
    print(f"")
    print(f"Abra o dashboard no navegador e ele vai usar o proxy automaticamente.")
    http.server.HTTPServer(('0.0.0.0', PORT), ProxyHandler).serve_forever()
