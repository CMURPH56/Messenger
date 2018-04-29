import threading, time, sys, socket, os, signal 

'''This is a simple direct messaging program that uses sockets 
   and threads, terminating standard import should shut down both sockets.
'''

class Reciever( threading.Thread):

	def __init__(self, sock):
		threading.Thread.__init__(self)
		self.sock = sock

	def run(self):
		msg_bytes = self.sock.recv(1024)
		while msg_bytes:
                        print(msg_bytes.decode(), end = '')
                        msg_bytes = self.sock.recv(1024)
		os._exit(0)
class Server:
			
	def sendMessage(sock):
		message = sys.stdin.readline() 
		while message:
			sock.send( message.encode() )
			message = sys.stdin.readline()
		os._exit(0)
	
	def connectServer():

		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
		serversocket.bind(('', int(sys.argv[2])))
		serversocket.listen(5)
		sock, addr = serversocket.accept()

		reciever = Reciever(sock)
		reciever.start()

		Server.sendMessage(sock)		
		serversocket.shutdown(SHUT_RDWR)

class Client:

	def sendMessage(sock):
		message = sys.stdin.readline() 
		while message:
			sock.send( message.encode() )
			message= sys.stdin.readline()
		os._exit(0)


	def connectClient(): 
		argc = len ( sys.argv ) 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		if argc == 3: 		
			server = sys.argv[2]
		else:
			server = 'localhost'
		sock.connect((server, int(sys.argv[1])))	

		reciever1 = Reciever(sock)
		reciever1.start()

		Client.sendMessage(sock)
	
if __name__ == "__main__":	
	
	arglen = len (sys.argv) 	# Get the amount of arguments passed.
	
	if (sys.argv[1]== '-l'): 	# Checks to see if the second argument is -l then it is a server
		Server.connectServer()
	else: 				# If not it is a client
		Client.connectClient()

