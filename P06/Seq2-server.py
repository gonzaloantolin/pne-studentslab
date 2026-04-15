from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import jinja2 as j
from pathlib import Path
import os

PORT = 8080

GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

# Jinja setup (lo copiamops d la wiki)
env = j.Environment(loader=j.FileSystemLoader("html"))

def read_html_file(filename, context=None):
    template = env.get_template(filename)
    return template.render(context or {})


class SeqHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        print(f"Requested path: {path}")


        if path == "/ping":
            html = read_html_file("ping.html")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())


        elif path == "/":
            html = read_html_file("index.html")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())


        elif path == "/get":
            query = parse_qs(parsed_path.query)

            if "n" in query:
                try:
                    n = int(query["n"][0])
                    if 0 <= n <= 4:
                        file_path = os.path.join("sequences", f"{GENES[n]}.txt")
                        with open(file_path, "r") as f:
                            sequence = f.read()
                        html = read_html_file("get.html", {"sequence": sequence,"n": n})
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


        elif path == "/gene":
            query = parse_qs(parsed_path.query)
            if "g" in query:
                try:
                    g = query["g"][0]
                    if g in GENES:
                        file_path = os.path.join("sequences", f"{g}.txt")
                        with open(file_path, "r") as f:
                            sequence = "".join(line.strip()for line in f if not line.startswith(">"))

                        gene = "\n".join(sequence[i:i + 60] for i in range(0, len(sequence), 60))
                        html = read_html_file("gene.html", {"gene_name": g,"gene": gene})
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