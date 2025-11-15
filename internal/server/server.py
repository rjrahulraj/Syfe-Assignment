from http.server import BaseHTTPRequestHandler, HTTPServer

class Server:
    def __init__(self, addr):
        self.addr = addr

    def start(self):
        host, port = self.addr.split(":")
        server = HTTPServer((host, int(port)), self.RequestHandler)
        server.serve_forever()

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello, World!")
