
try :

	import socket
	import os
	import time
	from binascii import hexlify 

except :

	print("error in python laberarys")

def packing():
	ipv4 = []
	for i in range(5):
		ip = input("enter ip >> ")
		ipv4.append(ip)
	with open("hosts_ip.txt" , "w") as file:
		for j in range(5):
			a = socket.inet_aton(ipv4[j])
			f=file.write(f"{a}\n")
	print("IPs has been packet")
	return file
def unpacking():

	with open("hosts_ip.txt" , "r") as file:
		with open("hosts_ip.txt" , "r") as file:
			for line in file:
				a = socket.inet_ntoa(line)
				f=file.write(f"{a}\n")

packing()







