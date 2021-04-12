import socket
import threading
# socket server using UDP protocol only for one clients 
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip="192.168.43.169"
port=1234
s.bind((ip,port))
print("\n\n\t\t*****WELCOME TO CHAT APPLICATION*****\n\n")
def recv():
	x=s.recvfrom(100)
	#clientip=x[1][0]
	msg=x[0].decode()
	if msg=="exit":
		exit()
	else:
		print("\033[1;32;40m \t\t\t"+msg)
def send():
	rep=input("\033[1;16;40m \t\t\tReply: ")
	if rep=="exit":
		byte=bytes(rep,'utf-8')
		exit_msg=rep.encode('utf-8')
		s.sendto(exit_msg,("192.168.43.2",1234))
		exit()
	else:

		b=bytes(rep,'utf-8')
		msg=rep.encode('utf-8')
		s.sendto(msg,("192.168.43.2",1234))
while True:
	recv()
	send()

