import io
import sys
import wave
import asyncio
import websockets
import socket
from .STT_Engine import STT_Engine

# Watson server class
class WatsonBridge():

	def __init__(self):
		self.stt = STT_Engine()
		self.loop = asyncio.new_event_loop()
		asyncio.set_event_loop(self.loop)

	def get_ip_address(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		ip = s.getsockname()[0]
		s.close()
		return ip

        #Function used to send informations to Watson via STT_Engine
	def runBridge(self, audio, websocket):
                result = self.stt.recognize(audio)
                print (result)
                if result["results"][0]["alternatives"][0]["transcript"] :
                        return (result)
                else :
                        return ("Error with Watson..")

        #Client listener
	async def listener(self, websocket, path):
                try:
                        print ("Listening to AVA client..")
                        audio = await websocket.recv()
                        result = self.runBridge(audio, websocket)
                        print ("Message received...")
                        await websocket.send(result["results"][0]["alternatives"][0]["transcript"])
                except:
                         print ("Error in listening to avaClient")
                         pass

	def run(self):
	    start_server = websockets.serve(self.listener, '0.0.0.0', 8766)
	    print("AVA WebSocket Server listening on {}:8766".format(self.get_ip_address()))
	    self.loop.run_until_complete(start_server)
	    self.loop.run_forever()

	# def stop(self):
	#     print('Stopping {0}...'.format(self.__class__.__name__))
	#     self.loop.stop()

def main():
	serv = WatsonBridge()
	print("AVA server launched")
	while True:
		serv.run()

