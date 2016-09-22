"""
Programi: Server side script
Author: Juan E Tenorio Arzola
Description: Defines the behavior of the server
"""

import socket
from threading import *
import polynomials
import decimal
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = ''
port = 11092
print (host)
print (port)

def Evaluate(Identifier, DataArray):
	#Identifier should only be 'S' or 'E'

	DataArray = DataArray.replace(Identifier,"")
	print('Received data: '+ DataArray)
	DataArray = DataArray.split(' ')
	print('After spliting: ')
	print(DataArray)
	Xvalue = float(DataArray[0])
	newValues = []
	for s in range(len(DataArray)-1):
		newValues.append(DataArray[s+1])
	print('In an int array: ')
		
	print(newValues)
	print("\nX-value: ")
	print(Xvalue)
	newValues = map(float, newValues)
	result = str(polynomials.evaluate(Xvalue,newValues))
	clientsocket.send("E"+result)
		
		
def Bisection(Identifier, DataArray):
	DataArray = DataArray.replace(Identifier,"")
	print("Received data: " + DataArray)
	DataArray = DataArray.split(' ')
	print("After Splitting: ")
	print(DataArray)
	aValue = float(DataArray[0])
	bValue = float(DataArray[1])
	tolerance = float(DataArray[-1])
	newValues= []
	
	#Transfering the values into a new array
	#This way I do not deal with the indexes

	for s in range(len(DataArray)-3):
			newValues.append(DataArray[s+2])
	newValues = map(float,newValues)
	
	print("As a float[]: ", newValues)
	print("a: " + str(aValue))
	print("b: " + str(bValue))
	print("tolerance: " + str(tolerance))
	

	result = (polynomials.bisection(aValue,bValue,newValues,tolerance))
	print(str(result))
	clientsocket.send("S"+str(result))
	
		
def Run():
		print("Some one is in!")
		typeF = clientsocket.recv(512)
		typeF = str(typeF)
		if typeF is None:
			raise Exception("Client did not send anything\n\n")
		elif typeF[0] =='n':
			return bool(0)	
		elif typeF[0] == 'E':
			Evaluate(typeF[0], typeF)
			return bool(1)
		elif typeF[0] == 'S':
			Bisection(typeF[0],typeF)
			return bool(1)
		else:
			clientsocket.send("Relally??....")
		


		
serversocket.bind((host, port))


serversocket.listen(5)
cl = bool(1)
print ('server started and listening\n\n')
(clientsocket, address) = serversocket.accept()
while cl == bool(1):
	
	print("Potential Calculation ahead!\n\n")
	try:
		cl = Run()
	except BaseException as error:
		print("X:An exception ocurred: {}".format(error))
print('\n.\n.\n.Closing due to request from client\n.\n.\n.')
clientsocket.close()
