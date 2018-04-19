#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from http.server import HTTPServer,CGIHTTPRequestHandler
# port = 8080
#
# httpd = HTTPServer(('',port),CGIHTTPRequestHandler)
# print("starting simple_httpd on port:" + str(httpd.server_port))
# httpd.serve_forever()



import sys
from http.server import HTTPServer,CGIHTTPRequestHandler

Handler = CGIHTTPRequestHandler
Server = HTTPServer
Protocol = "HTTP/1.0"
if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('127.0.0.1', port)
Handler.protocol_version = Protocol
httpd = Server(server_address, Handler)
print("Serving HTTP")
httpd.serve_forever()