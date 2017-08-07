#socket is a package through which two computers on same network can be connected

import socket , sys

s = socket.socket()

#gets the hostname of the computer hosting

host = socket.gethostname()

c = 10

#give the free port number

port = 10035

s.bind((host,port))

# 1 implie client connected can be one atmost 5 can be connected

s.listen(1)

#the following loops perform a simple chat but a small with an exception
#the message entered by server delivers to client after client sends a msg and viceversa

print "waiting for client"

print "please enter username"

a = raw_input()

while True:

	client,addr = s.accept()

	print "connected with the system %s" % str(addr)

	while (c):

		client.send(raw_input())

		we = client.recv(1024)
		print  we

		c = c - 1

	client.close()

