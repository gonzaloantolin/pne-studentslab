from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import jinja2 as j
from pathlib import Path
import os
import requests
from gpg.gpgme import gpgme_op_encrypt_ext_start
from P01.Seq1 import Seq

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
                chromo_name = data2["karyotype"][0]
                if not data2.get("top_level_region"):
                    html = read_html_file("error.html", {"message": "Missing species"})
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())
                    return

                top_level_region_data = data2["top_level_region"]
                chromosome = chromo_name
                found = False
                length = 0

                for i in top_level_region_data:
                    if i["name"] == chromosome:
                        found = True
                        length = i["length"]


                if found == False:
                    html = read_html_file("error.html", {"message": "Chromosome not found"})  # ✅ mensaje mejor
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())
                    return

                else:
                    html = read_html_file("ChromosomeLength.html", {"species": species_name,"karyotype": chromosome,"length": length})
                    self.send_response(200)

            else:
                html = read_html_file("error.html", {"message": "Error with species"})
                self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

        elif path == "/geneLookup":
            query = parse_qs(parsed_path.query)

            if not query.get("gene"):
                html = read_html_file("error.html", {"message": "Missing gene"})
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(html.encode())
                return

            gene = query["gene"][0]
            url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/" + gene + "?content-type=application/json;expand=1"
            reqs = requests.get(url)

            if reqs.status_code == 200:
                data = reqs.json()
                gene_id = data["id"]

                if not gene_id:
                    html = read_html_file("error.html", {"message": "Gene not found"})
                    self.send_response(404)
                else:

                    html = read_html_file("geneLookup.html", {"gene": gene, "gene_id": gene_id})
                    self.send_response(200)
            else:
                html = read_html_file("error.html", {"message": "Error with gene"})
                self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

        elif path == "/geneSeq":
            query = parse_qs(parsed_path.query)

            if not query.get("gene"):
                html = read_html_file("error.html", {"message": "Missing gene"})
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(html.encode())
                return

            gene = query["gene"][0]
            url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/" + gene + "?content-type=application/json;expand=1"
            reqs = requests.get(url)

            if reqs.status_code == 200:
                gene_data = reqs.json()
                gene_id = gene_data.get("id")

                if gene_id:
                    url2 = "https://rest.ensembl.org/sequence/id/" + gene_id + "?content-type=text/plain"
                    reqs2 = requests.get(url2)
                    if reqs2.status_code == 200:
                        sequence = reqs2.text
                        if sequence:
                            html = read_html_file("geneSeq.html", {"gene": gene, "sequence": sequence})
                            self.send_response(200)
                        else:
                            html = read_html_file("error.html", {"message": "Sequence not found"})
                            self.send_response(404)
                    else:
                        html = read_html_file("error.html", {"message": "Error with sequence"})
                        self.send_response(400)
                else:
                    html = read_html_file("error.html", {"message": "Gene not found"})
                    self.send_response(404)
            else:
                html = read_html_file("error.html", {"message": "Error with gene"})
                self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

        elif path == "/geneInfo":
            query = parse_qs(parsed_path.query)

            if not query.get("gene"):
                html = read_html_file("error.html", {"message": "Missing gene"})
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(html.encode())
                return

            gene = query["gene"][0]
            url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/"+ gene +"?content-type=application/json"
            reqs = requests.get(url)

            if reqs.status_code == 200:
                data = reqs.json()
                gene_start = data["start"]
                gene_end = data["end"]
                gene_id = data["id"]
                name = data["display_name"]

                if gene_start and gene_end and gene_id and name:
                    gene_length = gene_end - gene_start + 1
                    html = read_html_file("geneInfo.html", {"gene_start": gene_start, "gene_end": gene_end, "gene_id": gene_id, "name": name, "gene_length": gene_length})
                    self.send_response(200)
                else:
                    html = read_html_file("error.html", {"message": "Gene not found"})
                    self.send_response(404)
            else:
                html = read_html_file("error.html", {"message": "Error with gene"})
                self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

        elif path == "/geneCalc":
            query = parse_qs(parsed_path.query)

            if not query.get("gene"):
                html = read_html_file("error.html", {"message": "Missing gene"})
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(html.encode())
                return

            gene = query["gene"][0]
            url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/" + gene + "?content-type=application/json;expand=1"
            reqs = requests.get(url)

            if reqs.status_code == 200:
                gene_data = reqs.json()
                gene_id = gene_data.get("id")

                if gene_id:
                    url2 = "https://rest.ensembl.org/sequence/id/" + gene_id + "?content-type=text/plain"
                    reqs2 = requests.get(url2)
                    if reqs2.status_code == 200:
                        sequence = reqs2.text
                        if sequence:
                            seq = Seq(sequence)
                            length = len(seq)
                            composition = seq.composition()
                            html = read_html_file("geneCalc.html", {"gene": gene, "length": length,"A": composition["A"],"C": composition["C"],"G": composition["G"],"T": composition["T"]})
                            self.send_response(200)
                        else:
                            html = read_html_file("error.html", {"message": "Sequence not found"})
                            self.send_response(404)
                    else:
                        html = read_html_file("error.html", {"message": "Error with sequence"})
                        self.send_response(400)

                else:
                    html = read_html_file("error.html", {"message": "Gene not found"})
                    self.send_response(404)

            else:
                html = read_html_file("error.html", {"message": "Error with gene"})
                self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

        elif path == "/geneList":
            query = parse_qs(parsed_path.query)














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
