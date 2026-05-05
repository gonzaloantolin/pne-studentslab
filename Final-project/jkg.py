if req_lookup.status_code != 200:
        html = read_html_file("error.html", {"message": "Gene not found"})
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())
        return

    gene_data = req_lookup.json()
    gene_id = gene_data.get("id")

    # 🔹 TU CÓDIGO ORIGINAL (solo cambiando gene → gene_id)
    url = "https://rest.ensembl.org/sequence/id/" + gene_id + "?content-type=text/plain"
    reqs = requests.get(url)

    if reqs.status_code == 200:
        sequence = reqs.text   # ✅ en vez de json()

        if not sequence:
            html = read_html_file("error.html", {"message": "Sequence not found"})
            self.send_response(404)
        else:
            html = read_html_file("geneSeq.html", {"gene": gene, "sequence": sequence})
            self.send_response(200)
    else:
        html = read_html_file("error.html", {"message": "Error with sequence"})
        self.send_response(400)

    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(html.encode())