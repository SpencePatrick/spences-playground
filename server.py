import os
import http.server
import socketserver
from bs4 import BeautifulSoup
from http import HTTPStatus
import requests

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):

        url = 'https://www.google.com/'
        r = requests.get(url)
        r.text
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Hello! you requested %s' % (r.text)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
