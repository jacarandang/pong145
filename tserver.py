import socket, threading

HOST = "192.168.254.103"
PORT = 8888

cl = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)

def getMessage(s, cl):
    while(1):
        a = s.recv(4096)
        print "|",a,"|"
        input()
        for c in cl:
            c.send(a)

while(1):
    (client, address) = s.accept()
    cl.append(client)
    threading.Thread(target = getMessage, args = (client, cl)).start()
    print "Connected", address
