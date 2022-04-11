# TP_CLIENT_SERVEUR

## PRINCIPE DU TP CLIENT SERVEUR 

Le Principe du TP client serveur est simple Client Serveur L e modèle client "serveur" est en fait un principe d’architecture informatique hiérarchisé en réseaux, interne avec TCP/IP ou externe sur Internet. Un ordinateur, ou un groupe d'ordinateurs, dénommé serveur, stocke la totalité des ressources partageables telles que données et traitements.

## Le Protocole utiliser 

C'est le protocole TCP/IP qui est un standard de communication entre deux processus qui garantie la fiabilite dans le transfert de donnees donc  Côté fonctionnement, la suite TCP/IP se base en partie sur l'adressage IP. Elle est capable de fractionner les informations échangées en paquets pour que les grosses données puissent être acceptées par les IP, et de contrôler les éventuelles erreurs de transmissions des données.

## Installation des Packages 

## installation du python3
sudo apt-get install python3

## Lien Git du Projet 
git clone https://github.com/vanexcel777/TP_CLIENT_SERVEUR.git

## Les etapes a suivres pour le faire sont :
### connection entre deux pc different 

```sh
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Create a TCP/IP socket
	server_address = ('localhost', 12345)
	print ('starting up on %s port %s' % server_address )
	sock.bind(server_address)
	
```

if faut changer le ``` localhost ``` en ``` ip_serveur ``` ssur les deux code python
```
server_address = ('10.27.0.1', 12345)

```
puis executer les codes

```client
python3 clientSimple.py
```

```server
python3 serverSimple.py
```


### connection en local

-> ouvrir deux terminal different 

-> executer les deux  codes pythons

```client
python3 clientSimple.py
```

```server
python3 serverSimple.py
```


### instruction

-> mettre un fichier dans la meme repetroire  ou se trouve le code python

-> le fichier doit  avoir un contenue qui est  image , texte 


creer un fichier text (ex: mess.txt)
```sh
touch mess.txt
```
ecrire le message dans le fichier text (mess.txt)





