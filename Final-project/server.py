from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import jinja2 as j
from pathlib import Path
import os
import requests

PORT = 8080

env = j.Environment(loader=j.FileSystemLoader("html"))

def read_html_file(filename, context=None):
    template = env.get_template(filename)
    return template.render(context or {})

class SeqHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        print(f"Requested path: {path}")

        if path == "/":
            html = read_html_file("index.html")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())



        elif path == "/listSpecies":
            query = parse_qs(parsed_path.query)
            url = "https://rest.ensembl.org/info/species?content-type=application/json"
            reqs = requests.get(url)
            if reqs.status_code == 200:
                data = reqs.json()
                species_data = data["species"]
                species = [specie["name"] for specie in species_data]
                total = len(species)
                limit_value = "None"
                if query.get("limit"):
                    limit_str = query["limit"][0]
                    try:
                        limit = int(limit_str.strip())
                        species = species[:limit]
                        limit_value = limit
                    except ValueError:
                        html = read_html_file("error.html", {"message": "Invalid limit"})
                        self.send_response(400)
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write(html.encode())
                        return
                html = read_html_file("species.html",{"species": species, "total": total, "limit": limit_value})
                self.send_response(200)

            else:
                html = read_html_file("error.html", {"message": "Error fetching species"})
                self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

        else:
            html = read_html_file("error.html")
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

if __name__ == "__main__":
    server = HTTPServer(("", PORT), SeqHandler)
    print(f"Server running on http://localhost:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        server.server_close()

