#socket client using UDP protocol  
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverip="192.168.43.169"
serverport=1234
s.bind(("192.168.43.2",1234))
print("\n\n\t\t*****WELCOME TO CHAT APPLICATION*****\n\n")
def send():
	msg=input("\033[1;16;40m \t\t\tSend Msg : ")
	if msg=="exit":
                byte = bytes(msg, 'utf-8')
                exit_msg = msg.encode('utf-8')
                s.sendto(exit_msg,(serverip,serverport))
    
                exit()
	else:
		b = bytes(msg, 'utf-8')	
		msg_final = msg.encode('utf-8')
		s.sendto(msg_final,(serverip,serverport))
def recv():
        x=s.recvfrom(100)
        msg=x[0].decode()
        if msg == "exit":
            exit()
        else:
            print("\033[1;32;40m \t\t\t"+msg)
while True:
	send()
	recv()
