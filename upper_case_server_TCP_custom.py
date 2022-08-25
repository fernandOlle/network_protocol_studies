# Course: Computer Networks
# Prof. Guilherme Correa
# Federal University of Pelotas (UFPEL)
# AGO 2022
# Author: fernandOlle
# Example of UDP application
# Lower case to upper case converter (server side)
# Requirements: Python3

from http import server
from socket import *

serverIP = '25.3.46.249'  # localhost or your server IP address
serverPort = 9998	# use the port number you wish (higher than 1023)

serverSocket = socket(AF_INET,SOCK_STREAM)	# creates a socket (server side)
serverSocket.bind((serverIP, serverPort))	# bind() associates the socket with its local address [bind() is used in the server side]
serverSocket.listen(1)
print("Server is on!")

while 1:
  connectionSocket, addr = serverSocket.accept()
  message, addr = connectionSocket.recvfrom(1500)		# 1500 bytes are read from the UDP socket
  decodedMessage = message.decode()
  modifiedMessage = decodedMessage.upper()
  print(modifiedMessage)
  encodedMessage = modifiedMessage.encode()
  connectionSocket.send(encodedMessage)
  connectionSocket.close()
