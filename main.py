from http.server import HTTPServer, BaseHTTPRequestHandler
import requestHandler
import models


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    # MyRequestHandler = requestHandler.RequestHandler
    models.initiate_mongo()
    run(HTTPServer, requestHandler.RequestHandler)
