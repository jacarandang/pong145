import socket
import threading

import ListeningThread
import TalkingThread
class Client:
		
	HOST = "127.0.0.1"
	PORT = 8888
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	
	t1 = TalkingThread.TalkingThread()
	t2 = ListeningThread.ListeningThread()
	
	t1.start()
	t2.start()
	
	
	#data = s.recv(1024)
	#data = bytes.decode(data)

	#print(data)

	input("")
	

	