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
                species = [specie["common_name"] for specie in species_data]
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
                html = read_html_file("error.html", {"message": "Error with species"})
                self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

        elif path == "/karyotype":

            query = parse_qs(parsed_path.query)
            url = "https://rest.ensembl.org/info/species?content-type=application/json"
            reqs = requests.get(url)

            if reqs.status_code == 200:
                data = reqs.json()
                species_data = data["species"]

                if not query.get("species"):
                    html = read_html_file("error.html", {"message": "Missing species"})
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())
                    return

                species_name = query["species"][0]
                found = False
                for specie in species_data:
                    if specie["common_name"] == species_name:
                        found = True

                if found == False:
                    html = read_html_file("error.html", {"message": "Species not found"})
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())
                    return

                url2 = "https://rest.ensembl.org/info/assembly/" + species_name + "?content-type=application/json"
                reqs2 = requests.get(url2)

                if reqs2.status_code == 200:
                    data2 = reqs2.json()
                    karyotype = data2["karyotype"]

                    html = read_html_file("karyotype.html", {"species": species_name, "karyotype": karyotype,})
                    self.send_response(200)

                else:
                    html = read_html_file("error.html", {"message": "Error with karyotype"})
                    self.send_response(400)

            else:
                html = read_html_file("error.html", {"message": "Error with species"})
                self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

        elif path == "/chromosomeLength":
            query = parse_qs(parsed_path.query)
            species_name = query["species"][0]
            url2 = "https://rest.ensembl.org/info/assembly/" + species_name + "?content-type=application/json"
            reqs2 = requests.get(url2)

            if reqs2.status_code == 200:
                data2 = reqs2.json()
                if not data2.get("top_level_region"):
                    html = read_html_file("error.html", {"message": "Missing species"})
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())
                    return

                top_level_region_data = data2["top_level_region"] ##########
                chromosome = data2["top_level_region"][0]
                found = False
                for i in top_level_region_data:
                    if i["name"] == chromosome:
                        found = True

                if found == False:
                    html = read_html_file("error.html", {"message": "Species not found"})
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())
                    return

                #url3 = "https://rest.ensembl.org/info/assembly/" + species_name + "?content-type=application/json"
                #reqs2 = requests.get(url2)

                else:
                    html = read_html_file("error.html", {"message": "Error with karyotype"})
                    self.send_response(400)

            else:
                html = read_html_file("error.html", {"message": "Error with species"})
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

