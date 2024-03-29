import socket
import select
import sys
import threading

import socket, threading

HOST = "localhost"
PORT = 8888

class Client:

	def __init__(self, host = HOST, port = PORT):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		print("Connecting to Server")
		self.socket.connect((host, int(port)))
		print("Connected")
		self.messageList = []
		self.connected = True
		self.kill = False

	def listen(self):
		while(True):
			if self.kill:
				break
			try:
				msg = self.socket.recv(1024)
				msgs = msg.split("\n")
			except:
				print "Server Disconnected"
				self.socket.close()
				self.connected = False
				break
			for message in msgs:
				if message == "": continue
				if message == "QUIT":
					self.socket.shutdown(socket.SHUT_RDWR)
					self.socket.close()
					self.kill = True
				self.messageList.append(message)

	def begin_listening(self):
		threading.Thread(target = self.listen).start()

	def send(self, msg):
		self.socket.send(msg+"\n")

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
		a = self.messageList
		self.messageList = []
		return a

	def push_back(self, msg):
		self.messageList = [msg] + self.messageList

	def kill_all(self):
		self.kill = True
		self.socket.close()

# class Client:
# 	def client():
# 		HOST = "127.0.0.1"
# 		PORT = 8888
# 		#HOST = input("Input HOST")
# 		#PORT = int(input("Input PORT"))
#
# 		csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 		csocket.connect((HOST, PORT))
#
# 		sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# 		def send_msg(sock):
# 			while 1:
# 				message = sys.stdin.readline()
# 				#sock.send(str.encode(message))
# 				sock.send(message)
# 				#sock.sendto(data, target)
# 				if "quit" in message:
# 					break
#
# 		def recv_msg(sock):
# 			while 1:
# 				data = sock.recv(1024)
# 				#data = bytes.decode(data)
# 				if "quit" in data:
# 					print("bye")
# 					break
# 				else :
# 					print(data)
#
# 		threading.Thread(target=send_msg, args=(csocket,)).start()
# 		threading.Thread(target=recv_msg, args=(csocket,)).start()
#
# 		#while(1):
# 		#	sockets = [socket.socket(), csocket]
# 		#	#message = input()
#
# 		#	read, write, error = select.select(sockets, [], [])
# 		#	for s in read:
# 		#		if(s == csocket):
# 		#			data = csocket.recv(1024)
# 		#			if not data :
# 		#				print ("\nDisconnected from chat server")
# 		#				sys.exit()
# 		#			else :
# 		#				#print data
# 		#				sys.stdout.write(bytes.decode(data))
# 		#				sys.stdout.write('[Me] '); sys.stdout.flush()
# 		#			data = bytes.decode(data)
# 		#			print(data)
# 		#		else:
# 		#			message = sys.stdin.readLine()
# 		#			csocket.send(str.encode(message))
#
# 		#t1 = TalkingThread.TalkingThread()
# 		#t2 = ListeningThread.ListeningThread()
#
# 		#t1.start()
# 		#t2.start()
#
#
# 		#data = s.recv(1024)
# 		#data = bytes.decode(data)
#
# 		#print(data)
#
# 		#input("")
#
# 	if __name__ == "__main__":
# 		sys.exit(client())
