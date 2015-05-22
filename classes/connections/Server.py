import socket, threading

HOST = "localhost"
PORT = 8888

class Server:

	def __init__(self, host = HOST, port = PORT):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		print("Starting Server")
		self.socket.bind((host, int(port)))
		self.socket.listen(4)
		print("Server Initialized")
		self.player1 = None
		self.player2 = None
		self.messageList = []
		self.quit = False

	def listen(self, client):
		while(True):
			if self.quit:
				break
			try:
				msg = client.recv(1024)
				if not msg:
					client.close()
					break
				msgs = msg.split("\n")
			except:
				print "Client Disconnected"
				client.close()
				break
			for message in msgs:
				if message == "": continue
				if message == "QUIT":
					client.close()
					self.quit = True
				self.messageList.append((client, message))

	def begin_listening(self):
		threading.Thread(target = self.listen, args = (self.player1, )).start()
		threading.Thread(target = self.listen, args = (self.player2, )).start()

	def start(self):
		client, address = self.socket.accept()
		print address, "as player1 connected"
		self.player1 = client
		self.player1.send("1")

		client, address = self.socket.accept()
		print address, "as player 2 connected"
		self.player2 = client
		self.player2.send("2")

	def send_to_all(self, msg):
		self.player1.send(msg)
		self.player2.send(msg)

	def send_to_player1(self, msg):
		if self.player1 is not None:
			self.player1.send(msg)

	def send_to_player2(self, msg):
		if self.player2 is not None:
			self.player2.send(msg)

	def get_message(self):
		if len(self.messageList) == 0:
			return None
		return self.messageList.pop(0)

	def wait_message(self):
		while(1):
			if len(self.messageList) == 0:
				continue
			return self.messageList.pop(0)

	def get_all(self):
		a = self.messageList[:]
		self.messageList = []
		return a

	def kill_all(self):
		self.quit = True

# #clients list
# sockets = []
# def server():
# 	ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	print("Starting server...")
#
# 	ssocket.bind((HOST, PORT))
# 	ssocket.listen(5)
# 	print("Server initialized")
#
# 	sockets.append(ssocket)
#
# 	print("Waiting for a connection..")
#
# 	while(1):
# 		# 4th is timeout
# 		read, write, error = select.select(sockets, [], [], 0)
#
# 		for s in read:
# 			# new client
# 			if s == ssocket:
# 				client, address = ssocket.accept()
# 				sockets.append(client)
# 				print "Client (%s, %s) connected" % address
# 				#print(str(client) + " connected!")
# 				sendToAll(ssocket, client, "[%s:%s] joined\n" % address)
# 			# new message
# 			else:
# 				try:
# 					data = s.recv(1024)
# 					if data:
# 						#data = bytes.decode(data)
# 						print(data)
# 						if "quit" in data:
# 							#s.send(str.encode("quit"))
# 							s.send("quit")
# 						else:
# 							sendToAll(ssocket, s, data)
# 					else:
# 						if s in sockets:
# 							sockets.remove(s)
# 						sendToAll(ssocket, s, "Client (%s, %s) is offline\n" % address)
# 				except:
# 					sendToAll(ssocket, s, "Client (%s, %s) is offline\n" % address)
# 					continue
# 	ssocket.close()
#
# def sendToAll(ssocket, sock, message):
# 	for s in sockets:
# 		if (s!=ssocket):
# 			try:
# 				#s.send(str.encode(message))
# 				s.send(message)
# 			except:
# 				s.close()
# 				if (s in sockets):
# 					sockets.remove(s)
#
# if __name__ == "__main__":
# 	sys.exit(server())
#
# >>>>>>> connection
