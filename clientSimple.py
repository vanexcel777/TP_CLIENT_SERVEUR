import socket
import sys
import os
from collections import Counter


def bitParite_pair( b_array):
	#b_array doit être un bytearray
	#fonction qui retourne un bytearray avec le bit de parité pair

	res = bytearray()

	for i in range(len(b_array)):
		#convertir l'element en binaire
		octet = bin(b_array[i])[2:]


		if (Counter(octet)['1'] % 2 == 0):
			#le nombre de 1 est pair
			res.append(int('0' + octet,2))
		else:
			#le nombre de 1 est impair
			res.append(int('1' + octet,2))
	return res



def bitParite_impair(b_array):
	#b_array doit être un bytearray
	#fonction qui retourne un bytearray avec le bit de parité impair
	res = bytearray()
	for i in range(len(b_array)):

                #convertir l'element en binaire
                octet = bin(b_array[i])[2:]


                if (Counter(octet)['1'] % 2 == 0):
                        #le nombre de 1 est pair
                        res.append(int('1' + octet,2))
                else:
                        #le nombre de 1 est impair
                        res.append(int('0' + octet,2))

	return res

def somme_fletcher(fil):
	checksum1 = []
	checksum2 = []
	somme = 0

	#faire le tableau checksum1
	for i in texte:
		#ord() retourne la valeur acsii
		valeur = ord(i)
		somme += valeur
		checksum1.append(somme % 65535)


	#faire le tableau checksum2
	counter = 0
	somme = 0
	for i in texte:
		somme += checksum1[counter]
		checksum2.append(somme % 65535)
		counter += 1
	#retourner un dictionnaire des deux checksums
	tableau = [checksum1[len(checksum1) - 1], checksum2[len(checksum2) - 1]]
	return tableau


	
	
def recevoir_fichier(data):
	data = data.decode()	               
	nom = data.split("nom")[1]
	nom = nom.split("octet")[0]
	taille = data.split("octet")[1]
	print('file a recevoir: ' + nom + " ( " + taille +"   octets )")
	
	taille = int (taille)
	acc = input('acceptez-vous [o/n]: ')
	
	if acc == "o" and taille != 0:
		sock.send(b'accepte')
		f=sock.recv(10240)
		if f:

			with open("file_recu",'wb') as fl:
				fichier = fl.write(f)	
				
			print("fichier recu: "+ nom)

			
		else:
			print("file no send !!")
	                			                
	else:
		print ("fichier non-accepter")           	
	     	

if __name__ == '__main__':
	
	# Create a TCP/IP socket
	sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# Connect the socket to the port where the server is listening
	server_address = ('localhost',12345)
	print('connecting to %s port %s' % server_address)
	sock.connect(server_address)
	msg='1234'
	
	try:
	    # Look for the response
	    data=sock.recv(1024) 
	    
	    print ( 'received: %s' % data.decode())
	    
	    while True:
	    	# Send data
	        message = input('This is the message: ')
	        if message == "":
	        	print("error!!!")
	        	break
	        	
	        print ('sending "%s"\n' % message )
	        sock.send(message.encode())
	        
	        data=sock.recv(1024)
	        
	        if data:
	            if message == "1":
	            	recevoir_fichier(data)
	            	break

	      
	            elif message == "2":
	            	recevoir_fichier(data)
	            	break
	            	
	            else:
	            	print("choisir entre 1 , 2 ou 3")
	            	continue
	                
	            
	        else:
	    	    print('no more data from')
	    	    break

	    	

	finally:
 	    print ( 'closing socket' )
 	    sock.close()



