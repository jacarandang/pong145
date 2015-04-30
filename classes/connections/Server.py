import socket
import threading

class Server:

	HOST = "127.0.0.1"
	PORT = 8888
	
	#clients list
	clients = []
	
	ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Starting server...")
	
	ssocket.bind((HOST, PORT))
	ssocket.listen(5)
	print("Server initialized")
	
	while(1):
		print("Waiting for a connection..")
		client, address = ssocket.accept()
		print("new connection from " + str(address))
		#client.send(str.encode("Shems Co!"))
		break
	


	