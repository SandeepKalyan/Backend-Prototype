import json
from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Set the response status code
        self.send_response(200)

        # Set the response headers
        self.send_header('Content-type', 'Initiation')

        self.end_headers()

        # Set the response content
        response = 'Hello'
        self.wfile.write(response.encode())

    def do_POST(self):
        print(self.path)
        self.send_header("header:", "Version-1")
        self.send_response(200, "Response body")
        self.end_headers()
