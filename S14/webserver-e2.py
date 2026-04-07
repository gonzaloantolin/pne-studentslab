import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8081

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        # Message to send back to the client
        if self.path == "/" or self.path == "/index.html":
            filename = "index.html"
            self.send_response(200)
        else:
            filename = "error.html"
            self.send_response(404)

        try:
            with open(filename, "r") as f:
                contents = f.read()

            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()
            self.wfile.write(contents.encode())

        except FileNotFoundError:
            self.send_response(500)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(contents.encode())

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
