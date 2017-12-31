import socket
from .STT_Engine import STT_Engine

# tornado 
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

# Watson server class
class SphinxBridge(tornado.websocket.WebSocketHandler):

        #Function used to send informations to Sphinx via STT_Engine
	def runBridge(self, audio):
                result = self.stt.recognize(audio)
                print(result)
                return (result)


	def open(self):
                try:
                        self.stt
                except:
                        self.stt = STT_Engine()
                print('Client IP:' + self.request.remote_ip)
                print('[new connection Accepted]')

	def on_message(self, message):
                result = self.runBridge(message)
                print ("Message received...")
                try:
                        self.write_message(result)
                except:
                        self.write_message("No message")

	def on_close(self):
                print('[connection closed]')


	def check_origin(self, origin):
                return True

application = tornado.web.Application([
    (r'/sphinx', SphinxBridge),
])


def main():
	print("AVA server launched")
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)
	myIP = socket.gethostbyname(socket.gethostname())
	print('*** AVA Websocket Server Started at %s/sphinx***' % myIP)
	tornado.ioloop.IOLoop.instance().start()
