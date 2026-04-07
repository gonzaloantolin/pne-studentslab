import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8081

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        # Default file for "/"
        if self.path == "/":
            filepath = Path("index.html")
        else:
            # Remove the leading "/"
            filepath = Path(self.path[1:])

        try:
            # Try to open requested file
            content = filepath.read_bytes()
            self.send_response(200)

        except FileNotFoundError:
            # If file does not exist → serve error.html
            filepath = Path("error.html")
            content = filepath.read_bytes()
            self.send_response(404)

        # Send headers
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(content))
        self.end_headers()

        # Send file content
        self.wfile.write(content)


# ------------------------
# Server MAIN program
# ------------------------

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()