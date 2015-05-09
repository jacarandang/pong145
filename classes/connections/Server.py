import socket
import select
import sys

#class Server:
	
HOST = "127.0.0.1"
PORT = 8888
	
#clients list
sockets = []
def server():
	ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Starting server...")
	
	ssocket.bind((HOST, PORT))
	ssocket.listen(5)
	print("Server initialized")
	
	sockets.append(ssocket)
	
	print("Waiting for a connection..")
	
	while(1):
		# 4th is timeout
		read, write, error = select.select(sockets, [], [], 0)
		
		for s in read:
			# new client
			if s == ssocket:
				client, address = ssocket.accept()
				sockets.append(client)
				print(str(client) + " connected!")
				sendToAll(ssocket, client, "[%s:%s] joined\n" % address)
			# new message
			else:
				try:
					data = s.recv(1024)
					if data:
						data = bytes.decode(data)
						sendToAll(ssocket, s, data)
					else: 
						if s in sockets:
							sockets.remove(s)
						sendToAll(ssocket, s, "Client (%s, %s) is offline\n" % address) 
				except:
					sendToAll(ssocket, s, "Client (%s, %s) is offline\n" % address) 
					continue
	ssocket.close()
		
def sendToAll(ssocket, sock, message):
	for s in sockets:
		if (s!=ssocket):
			try:
				s.send(str.encode(message))
			except:
				s.close()
				if (s in sockets):
					sockets.remove(s)
					
if __name__ == "__main__":
	sys.exit(server()) 
	