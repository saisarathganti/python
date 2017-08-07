import socket , sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'enter the hostname of the computer to be connected'
port = 10034
print "please enter your username"
b = raw_input()
s.connect((host,port))
print "you have got connected "
while (1):
	s.send(raw_input())
	we = s.recv(1024)
	print   we
s.close()

