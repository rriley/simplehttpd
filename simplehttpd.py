import SimpleHTTPServer
import SocketServer
import logging
import cgi

PORT = 8000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
        logging.info(self.headers)
	try:
		cl = int(self.headers['Content-Length'])
	except:
		cl = 0
	data = self.rfile.read(cl)
	logging.info(data)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

logging.basicConfig(filename='clist.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

Handler = ServerHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "Serving at port", PORT
httpd.serve_forever()
