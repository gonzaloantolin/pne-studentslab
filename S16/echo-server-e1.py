import http.server
import socketserver
import termcolor
from pathlib import Path
import urllib.parse

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        # ---- ROUTE: MAIN PAGE ----
        if self.path == "/":
            contents = Path('html/form-e1.html').read_text()
            self.send_html(contents, 200)

        # ---- ROUTE: ECHO ----
        elif self.path.startswith("/echo"):
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)

            message = params.get("message", [""])[0]

            contents = f"""
            <html>
                <body>
                    <h1>Echo Message</h1>
                    <p>{message}</p>
                    <br>
                    <a href="/">Main page</a>
                </body>
            </html>
            """

            self.send_html(contents, 200)

        # ---- ROUTE: ERROR ----
        else:
            contents = Path('html/error.html').read_text()
            self.send_html(contents, 404)

    # OPTIONAL: handle POST (recommended)
    def do_POST(self):
        if self.path == "/echo":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode()

            params = urllib.parse.parse_qs(post_data)
            message = params.get("message", [""])[0]

            contents = f"""
            <html>
                <body>
                    <h1>Echo Message</h1>
                    <p>{message}</p>
                    <br>
                    <a href="/">Back to form</a>
                </body>
            </html>
            """

            self.send_html(contents, 200)
        else:
            contents = Path('html/error.html').read_text()
            self.send_html(contents, 404)

    # ---- HELPER FUNCTION ----
    def send_html(self, contents, code):
        self.send_response(code)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())


# ------------------------
# SERVER
# ------------------------
Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()