# Course: Computer Networks
# Prof. Guilherme Correa
# Federal University of Pelotas (UFPEL)
# AGO 2022
# Author: fernandOlle
# Example of UDP application
# Lower case to upper case converter (client side)
# Requirements: Python3

from socket import *

serverIP = '25.3.250.88'  # localhost or your server IP address
serverPort = 9999		# use the port number you wish (higher than 1023)

clientSocket = socket(AF_INET, SOCK_STREAM)  # creates a socket (client side)

message = input('Enter your lower-case word: ')
encodedMessage = message.encode()
clientSocket.connect((serverIP, serverPort))
clientSocket.send(encodedMessage)     # sends the message to server (no need to use connect() before, since it is UDP)

modifiedMessage, serverIP = clientSocket.recvfrom(1500)         # 1500 bytes are read from the UDP socket
decodedMessage = modifiedMessage.decode()

print(decodedMessage)   # print received/decoded message

clientSocket.close()