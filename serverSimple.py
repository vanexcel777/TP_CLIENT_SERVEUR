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


def send_fichier():
	nom = input('inserer le nom du fichier: ')
	if nom != "":	
		try:
			fl =  open(nom,'rb') 
			fichier = fl.read() 
			test(nom, fichier)	
					
		except:	
			print("file no found  1!! \n" )
		
	else:
		print("file no found !!  2 \n" )
		 
			
def test(nom, fichier):
				
	octet = os.path.getsize(nom)
	
	conn.send(b'nom'+ nom.encode() + b'octet' + str(octet).encode())
	data = conn.recv(1024)
	
	if data.decode() == "accepte":
	
		print("envoye du fichier " + nom + "\n")
		conn.send(fichier)
		
		
	else:
		print("fichier non-accepter \n")
		
		
		
		
		
			


if __name__ == '__main__':
	
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Create a TCP/IP socket
	server_address = ('localhost', 12345)
	print ('starting up on %s port %s' % server_address )
	sock.bind(server_address)
	
	# Listen for incoming connections
	sock.listen(1)
	
	while True:
	    # Wait for a connection
	    print ('waiting for a connection' ) 
	    conn, addr =sock.accept()
	    
	    try:         
                print ( 'connection from ', addr ,"\n") 
                # Receive the data in small chunks and retransmit it
                message = "1- envoye fichier text \n \t  2- envoye image \n \t  3- exit"
                	
                conn.send(message.encode())
                
                while True :                  	
                                    
                    data = conn.recv(1024)
                    verification =  data.decode()
                                     
                    if (data):                                              
                        if verification == "1":                 
                        	send_fichier()              	
                        	break
                        
                        elif verification == "2":                       
                        	send_fichier()
                        	break
                        
                        elif verification == "3":
                        	break       
                        
                        else:
                        	mess="requete failed !!! \n\t choisissez entre 1 ou 2 ou 3 "
                        	conn.send(mess.encode())
                        	continue
                        	
                 		
                    	
                    else:
                    	print('no more data from', addr)
                    	break
                             
	    finally:
	    	conn.close()    
