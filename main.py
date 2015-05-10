from fresh_tomatoes import *
from movie import * 
import os
import BaseHTTPServer
import SocketServer
import webbrowser


PORT = 8000
Handler = BaseHTTPServer.BaseHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

#Path is where the final views go- this should look like a standard website structure
path = "./public/"
os.chdir( path )






print "serving at port", PORT
webbrowser.open('http://127.0.0.1:' + str(PORT) )
httpd.serve_forever()
