import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))

    def do_GET(self):
        self._send_response("Hello World")
        
    def do_POST(self):
        self._send_response("POSTED")
        exit()

httpd = HTTPServer(('localhost', 8000), RequestHandler)
#httpd.socket = ssl.wrap_socket (httpd.socket, certfile='server.pem', server_side=True)
httpd.serve_forever()