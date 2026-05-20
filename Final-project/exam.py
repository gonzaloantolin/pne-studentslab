elif path == "/geneRegion":
query = parse_qs(parsed_path.query)

if not query.get("gene") or not query.get("species"):
    html = read_html_file("error.html", {"message": "Missing parameters"})
    self.send_response(400)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(html.encode())
    return

gene = query["gene"][0]
species = query["species"][0]

url = "https://rest.ensembl.org/lookup/symbol/" + species + "/" + gene + "?content-type=application/json"
reqs = requests.get(url)

if reqs.status_code == 200:
    data = reqs.json()

    gene_id = data.get("id")
    gene_species = data.get("species")
    chromo = data.get("seq_region_name")
    gene_start = data.get("start")
    gene_end = data.get("end")

    if gene_id and gene_species and chromo and gene_start and gene_end:

        if gene_species != species:
            html = read_html_file("error.html", {"message": "Species does not match"})
            self.send_response(404)

        else:
            region_start = gene_start - 100000
            region_end = gene_end + 100000

            url2 = "https://rest.ensembl.org/overlap/region/human/" + str(chromo) + ":" + str(region_start) + "-" + str(
                region_end) + "?content-type=application/json;feature=gene"

            reqs2 = requests.get(url2)

            if reqs2.status_code == 200:
                region_data = reqs2.json()

                if region_data:

                    genes = ""

                    for region_gene in region_data:
                        region_gene_name = region_gene.get("external_name")
                        region_gene_id = region_gene.get("id")

                        genes += "<li>" + str(region_gene_name) + ": " + str(region_gene_id) + "</li>"

                    html = read_html_file("geneRegion.html", {
                        "gene": gene,
                        "gene_id": gene_id,
                        "chromosome": chromo,
                        "gene_start": gene_start,
                        "gene_end": gene_end,
                        "region_start": region_start,
                        "region_end": region_end,
                        "genes": genes
                    })

                    self.send_response(200)

                else:
                    html = read_html_file("error.html", {"message": "No genes found"})
                    self.send_response(404)

            else:
                html = read_html_file("error.html", {"message": "Error with region"})
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