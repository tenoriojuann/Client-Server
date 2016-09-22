"""
Programi: Server side script
Author: Juan E Tenorio Arzola
Description: Defines the behavior of the server
"""

import socket
from threading import *
import polynomials

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = ''
port = 11092
print (host)
print (port)

def Evaluate(Identifier, DataArray):
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
	newValues = map(int, newValues)
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
	tolerance = DataArray[-1]
	tolerance = float(eval(tolerance))
	newValues= []
		#Checking for ints, both positive and negative in the array
		#While skipping the first two and last values since they correspond
		#to a, b, and the tolerance
	for s in range(len(DataArray)-3):
			newValues.append(DataArray[s+2])
	newValues = map(int,newValues)
	
	print("Array as an int[]: ")
	print(newValues)
	print("a: " + str(aValue))
	print("b: " + str(bValue))
	print("tolerance: " + str(tolerance))
	

	result = str(polynomials.bisection(aValue,bValue,newValues,tolerance))
	clientsocket.send("E"+result)
	
		
def Run():
		print("Some one is in!")
		typeF = clientsocket.recv(512)
		typeF = str(typeF)
		if typeF is None:
			raise Exception("Client did not send anything\n\n")
		print(typeF)
		elif typeF[0] == 'E':
			Evaluate(typeF[0], typeF)
		elif typeF[0] == 'S':
			Bisection(typeF[0],typeF)

		else:
			clientsocket.send("Relally??....")
		


		
serversocket.bind((host, port))


serversocket.listen(5)

print ('server started and listening\n\n')
(clientsocket, address) = serversocket.accept()
while 1:
	
	print("Potential Calculation ahead!\n\n")
	try:
		Run()
	except BaseException as error:
		print("X:An exception ocurred: {}".format(error))
clientsocket.close()