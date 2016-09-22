import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'cs3.kennesaw.edu'
port = 11092
data = ''

s.connect((host,port))



def SyntaxCheck(Identifier, DataArray):
	DataArray = DataArray.replace(Identifier,"")
	DataArray = DataArray.split(' ')
	checkSyntax = bool(0)
	print(DataArray)
	if(len(DataArray) > 1):
		try:
			map(float,DataArray)
		except BaseException as error:
			print("X: An exception ocurred: ".format(error))
			checkSyntax = bool(1)
	else:
		print("X: The length is not appropiate")
		checkSyntax = bool(1)
	
	return checkSyntax





cl = bool(1)
while cl == bool(1):
	answer = raw_input("Do you want to calculate something? (Y/N)")
	if answer == 'y':
		typeF = raw_input("Enter a string: ")
		check = SyntaxCheck(typeF[0], typeF)
		if( check == bool(0)):
			s.send(typeF)
			data = s.recv(512).decode()
			print(data)
		answer = raw_input("DO you want to calculate something else?(Y/N)\n\n")
	elif answer =='n' or answer =='N':
		cl = bool(0)
		s.send(answer)
	else:
		print("that was not one of the options")
print('\n\n\nClosing the connection now\n\n\n')
s.close ()