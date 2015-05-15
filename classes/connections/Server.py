import socket, threading

HOST = "localhost"
PORT = 8000

class Server:

    def __init__(self, host = HOST, port = PORT):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.s.bind((host, port))
        self.s.listen(6)
        self.messageList = []

    def sendToAll(self, msg):
        for c in self.clients:
            c.send(msg)

    def begin(self):
        cl1, address1 = self.s.accept()
        print "One player connected at", address1
        self.clients.append(cl1)
        cl2, address2 = self.s.accept()
        print "One player connected at", address2
        self.clients.append(cl2)
        print "Two players connected, ready"

    def listen(self, client):
        while(1):
            a = client.recv(1024)
            self.messageList.append(a)
    def beginListen(self):
        for cl in self.clients:
            threading.Thread(target = self.listen, args = (cl))
        while(1):
            pass
