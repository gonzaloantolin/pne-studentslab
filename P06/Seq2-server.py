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

                        with open("html/get.html", "r") as f:
                            content = f.read()

                        content = content.replace("{{sequence}}", sequence)
                        content = content.replace("{{n}}", str(n))

                        self.send_response(200)
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write(content.encode())

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