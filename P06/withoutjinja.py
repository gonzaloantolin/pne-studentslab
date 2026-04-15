from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

PORT = 8080


SEQUENCES = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"
]
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

class SeqHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        print(f"Requested path: {path}")

        if path == "/ping":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            html = """
            <!DOCTYPE html>
            <html>
            <body>
                <h1>PING OK!</h1>
                <h1>The Seq 2 server is running</h1>
                <a href="/">Go to main page</a>
            </body>
            </html>
            """
            self.wfile.write(html.encode())

        elif path == "/":
            try:
                with open("html/index.html", "r") as f:
                    content = f.read()

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode())

            except FileNotFoundError:
                self.send_error(404, "index.html not found")


        elif path == "/get":
            query = parse_qs(parsed_path.query)
            if "n" in query:
                try:
                    n = int(query["n"][0])
                    if 0 <= n <= 4:
                        sequence = SEQUENCES[n]
                        html = read_html_file("get.html", {"sequence": sequence, "n":n})
                        self.send_response(200)
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write(html.encode())
                    else:
                        raise ValueError
                except:
                    self.send_error(400, "Invalid sequence number")
            else:
                self.send_error(400, "Missing parameter n")

        else:
            try:
                with open("html/error.html", "r") as f:
                    content = f.read()

                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode())

            except FileNotFoundError:
                self.send_error(404, "error.html not found")


if __name__ == "__main__":
    server = HTTPServer(("", PORT), SeqHandler)
    print(f"Server running on http://localhost:{PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        server.server_close()



elif path == "/gene":
    query = parse_qs(parsed_path.query)

    if "g" in query:
        try:
            g = query["g"][0]

            if g in GENES:
                file_path = os.path.join("sequences", f"{g}.txt")

                with open(file_path, "r") as f:
                    gene = f.read()

                html = read_html_file("gene.html", {
                    "gene_name": g,
                    "gene": gene
                })

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(html.encode())

            else:
                raise ValueError

        except:
            self.send_error(400, "Invalid gene")

    else:
        self.send_error(400, "Missing parameter g")