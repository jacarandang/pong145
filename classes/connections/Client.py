import socket
import select
import sys
import threading

class Client:
	def client():
		HOST = "127.0.0.1"
		PORT = 8888
		#HOST = input("Input HOST")
		#PORT = int(input("Input PORT"))
		
		csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		csocket.connect((HOST, PORT))
		
		sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		def send_msg(sock):
			while 1:
				message = sys.stdin.readline()
				sock.send(str.encode(message))
				#sock.sendto(data, target)
				if "quit" in message:
					break

		def recv_msg(sock):
			while 1:
				data = sock.recv(1024)
				data = bytes.decode(data)
				if "quit" in data:
					print("bye")
					break
				else :
					print(data)

		threading.Thread(target=send_msg, args=(csocket,)).start()  
		threading.Thread(target=recv_msg, args=(csocket,)).start()
		
		#while(1):
		#	sockets = [socket.socket(), csocket]
		#	#message = input()
			
		#	read, write, error = select.select(sockets, [], [])
		#	for s in read:
		#		if(s == csocket):
		#			data = csocket.recv(1024)
		#			if not data :
		#				print ("\nDisconnected from chat server")
		#				sys.exit()
		#			else :
		#				#print data
		#				sys.stdout.write(bytes.decode(data))
		#				sys.stdout.write('[Me] '); sys.stdout.flush() 
		#			data = bytes.decode(data)
		#			print(data)
		#		else:
		#			message = sys.stdin.readLine()
		#			csocket.send(str.encode(message))
			
		#t1 = TalkingThread.TalkingThread()
		#t2 = ListeningThread.ListeningThread()
		
		#t1.start()
		#t2.start()
		
	
		#data = s.recv(1024)
		#data = bytes.decode(data)

		#print(data)

		#input("")
	
	if __name__ == "__main__":
		sys.exit(client()) 
	