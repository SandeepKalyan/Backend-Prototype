from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        print(self.client_address)

        # Home & User APIs
        if self.path == '/':
            print(self.path)
        elif self.path == '/logout':
            print(self.path)
        elif self.path == '/users':
            print(self.path)

        # Cart APIs
        elif self.path == '/viewcart':
            print(self.path)
        elif self.path == '/buycart':
            print(self.path)
        elif self.path == '/orders':
            print(self.path)

        #
        elif self.path == '/home':
            print(self.path)

        else:
            print(self.path)

        # Set the response status code
        self.send_response(200)

        # Set the response headers
        self.send_header('Content-type', 'Initiation')

        self.end_headers()

        # Set the response content
        response = 'Hello'
        self.wfile.write(response.encode())

    def do_POST(self):
        if self.path == '/':
            print(self.path)
        elif self.path == '/register':
            print(self.path)
        elif self.path == '/login':
            print(self.path)
        elif self.path == '/cartload':
            print(self.path)
        elif self.path == '/removefromcart':
            print(self.path)
        elif self.path == '/buynow':
            print(self.path)
