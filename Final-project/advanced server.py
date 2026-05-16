from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import jinja2 as j
import requests
import json
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
        query = parse_qs(parsed_path.query)
        json_mode = query.get("json") == ["1"]
        print(f"Requested path: {path}")

        if path == "/":
            html = read_html_file("index.html")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

        elif path == "/listSpecies":
            url = "https://rest.ensembl.org/info/species?content-type=application/json"
            reqs = requests.get(url)

            if reqs.status_code == 200:
                data = reqs.json()
                species_data = data["species"]
                species = [specie["common_name"] for specie in species_data]
                total = len(species)
                limit_value = "None"

                if query.get("limit"):
                    limit = int(query["limit"][0])
                    species = species[:limit]
                    limit_value = limit

                if json_mode:

                    response = {"total": total, "limit": limit_value, "species": species}

                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode())

                else:

                    html = read_html_file("species.html", {
                        "species": species,
                        "total": total,
                        "limit": limit_value
                    })

                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())

        elif path == "/karyotype":

            species_name = query["species"][0]

            url = "https://rest.ensembl.org/info/assembly/" + species_name + "?content-type=application/json"
            reqs = requests.get(url)

            if reqs.status_code == 200:

                data = reqs.json()
                karyotype = data["karyotype"]

                if json_mode:

                    response = {
                        "species": species_name,
                        "karyotype": karyotype
                    }

                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode())

                else:

                    html = read_html_file("karyotype.html", {
                        "species": species_name,
                        "karyotype": karyotype
                    })

                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())

        elif path == "/chromosomeLength":

            species_name = query["species"][0]

            url = "https://rest.ensembl.org/info/assembly/" + species_name + "?content-type=application/json"
            reqs = requests.get(url)

            if reqs.status_code == 200:

                data = reqs.json()
                chromosome = data["karyotype"][0]
                top_level_region_data = data["top_level_region"]
                length = 0

                for i in top_level_region_data:
                    if i["name"] == chromosome:
                        length = i["length"]

                if json_mode:

                    response = {
                        "species": species_name,
                        "chromosome": chromosome,
                        "length": length
                    }

                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode())

                else:

                    html = read_html_file("ChromosomeLength.html", {
                        "species": species_name,
                        "karyotype": chromosome,
                        "length": length
                    })

                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())

        elif path == "/geneLookup":

            gene = query["gene"][0]

            url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/" + gene + "?content-type=application/json"
            reqs = requests.get(url)

            if reqs.status_code == 200:

                data = reqs.json()
                gene_id = data["id"]

                if json_mode:

                    response = {
                        "gene": gene,
                        "gene_id": gene_id
                    }

                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode())

                else:

                    html = read_html_file("geneLookup.html", {
                        "gene": gene,
                        "gene_id": gene_id
                    })

                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())

        elif path == "/geneSeq":

            gene = query["gene"][0]

            url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/" + gene + "?content-type=application/json"
            reqs = requests.get(url)

            if reqs.status_code == 200:

                gene_data = reqs.json()
                gene_id = gene_data["id"]

                url2 = "https://rest.ensembl.org/sequence/id/" + gene_id + "?content-type=text/plain"
                reqs2 = requests.get(url2)

                sequence = reqs2.text

                if json_mode:

                    response = {
                        "gene": gene,
                        "sequence": sequence
                    }

                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode())

                else:

                    html = read_html_file("geneSeq.html", {
                        "gene": gene,
                        "sequence": sequence
                    })

                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())

        elif path == "/geneInfo":

            gene = query["gene"][0]

            url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/" + gene + "?content-type=application/json"
            reqs = requests.get(url)

            if reqs.status_code == 200:

                data = reqs.json()

                gene_start = data["start"]
                gene_end = data["end"]
                gene_id = data["id"]
                name = data["display_name"]

                gene_length = gene_end - gene_start + 1

                if json_mode:

                    response = {
                        "gene_start": gene_start,
                        "gene_end": gene_end,
                        "gene_id": gene_id,
                        "name": name,
                        "gene_length": gene_length
                    }

                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode())

                else:

                    html = read_html_file("geneInfo.html", {
                        "gene_start": gene_start,
                        "gene_end": gene_end,
                        "gene_id": gene_id,
                        "name": name,
                        "gene_length": gene_length
                    })

                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(html.encode())

        elif path == "/geneCalc":

            gene = query["gene"][0]

            url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/" + gene + "?content-type=application/json"
            reqs = requests.get(url)

            gene_data = reqs.json()
            gene_id = gene_data["id"]

            url2 = "https://rest.ensembl.org/sequence/id/" + gene_id + "?content-type=text/plain"
            reqs2 = requests.get(url2)

            sequence = reqs2.text

            seq = Seq(sequence)
            length = len(seq)
            composition = seq.composition()

            if json_mode:

                response = {
                    "gene": gene,
                    "length": length,
                    "A": composition["A"],
                    "C": composition["C"],
                    "G": composition["G"],
                    "T": composition["T"]
                }

                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())

            else:

                html = read_html_file("geneCalc.html", {
                    "gene": gene,
                    "length": length,
                    "A": composition["A"],
                    "C": composition["C"],
                    "G": composition["G"],
                    "T": composition["T"]
                })

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(html.encode())

        elif path == "/geneList":

            chromo = query["chromo"][0]
            start = query["start"][0]
            end = query["end"][0]

            url = "https://rest.ensembl.org/overlap/region/human/" + chromo + ":" + start + "-" + end + "?content-type=application/json;feature=gene"
            reqs = requests.get(url)

            if reqs.status_code == 200:

                gene_data = reqs.json()
                genes = []

                for gene in gene_data:

                    gene_name = gene.get("external_name")
                    gene_id = gene.get("id")

                    genes.append(str(gene_name) + ": " + gene_id)

                if json_mode:

                    response = {
                        "chromosome": chromo,
                        "genes": genes
                    }

                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode())

                else:

                    genes_html = ""

                    for g in genes:
                        genes_html += "<li>" + g + "</li>"

                    html = read_html_file("geneList.html", {
                        "chromo": chromo,
                        "genes": genes_html
                    })

                    self.send_response(200)
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