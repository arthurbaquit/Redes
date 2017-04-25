import socket
import time

serverName = raw_input('Digite o IP do servidor: ')
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = raw_input('Digite a mensagem ou digite 0 para sair: ')
while (message != '0'):
	clientSocket.sendto(message,(serverName, serverPort))
	time.sleep(0.5)
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print modifiedMessage
	message = raw_input('Digite a mensagem ou digite 0 para sair: ')
clientSocket.close()
