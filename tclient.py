import socket, threading

host = "localhost"
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print "Connected"

def get_msg(s):
    while(1):
        try:
            a = s.recv(4096)
        except:
            print "Server Closed"
            break
        print a

def send_msg(s):
    while(1):
        print "Msg: "
        msg = raw_input()
        s.send(msg)


threading.Thread(target=get_msg, args = (s,) ).start()
threading.Thread(target=send_msg, args = (s,) ).start()
