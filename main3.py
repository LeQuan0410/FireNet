# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import time
import sys
import random
from subprocess import call



class c():
	black='\033[30m'
	red='\033[31m'
	green='\033[32m'
	orange='\033[33m'
	blue='\033[34m'
	purple='\033[35m'
	cyan='\033[36m'
	lightgrey='\033[37m'
	darkgrey='\033[90m'
	lightred='\033[91m'
	lightgreen='\033[92m'
	yellow='\033[93m'
	lightblue='\033[94m'
	pink='\033[95m'
	lightcyan='\033[96m'
	reset='\033[0m'

def info():
	print("""
 -- FireNet - 2023 DDoS attack script --
 Methods layer7:
 		HTTP GET - Get requests with threads 
	 	Cloudflare bypasses - CF bypass via cloudscraper
	 	HTTP POST - post requests with threads
	 	HTTP GET With proxies - get requests with proxies
	 	.onion-slam - custom method to DDoS .onion links via proxies
	 	Http-custom - Hits layer 4 and 7 (ip must accept http requests)

 	Methods layer4:
		Socket-TCP - TCP ddos over sockets
		UDP - UDP flood
		SYN - SYN attack
		Memcrashed (beta) - Memcrashed AMP attack

 	Tools:
		resolver - ip/domain resolver and more.

 	**MUCH MORE COMING SOON!**
 """)

def rgb():
	colors = ["\033[33m", "\033[35m", "\033[93m", "\033[31m", "\033[95m", "\033[36m", "\033[34m", "\033[32m"]
	rnb = random.choice(colors)
	return rnb

def toolsmenu():
	os.system('cls||clear')
	print(f"""
	                ╔═══════════════╗
	                ║     tools     ║
	╔═══════════════╩══════╦════════╩═══════════════╗
	║  resolver            ║  <empty>               ║
	║  <empty>             ║  <empty>               ║  
	║  <empty>             ║  <empty>               ║
	║  <empty>             ║  <empty>               ║
	║  <empty>             ║  <empty>               ║
	╚══════════════════════╩════════════════════════╝
	""")
	try:
		while (True):
			tools = input(f"{c.green}[FireNet{rgb()}@{c.purple}Root]$>{rgb()} ")
			if tools == "resolver":
				call(["python3", "./files/resolver.py"])
			elif tools == "home" or tools == "Home":
				main()
			else:
				print("Retype that dummy.")
	except KeyboardInterrupt:
		toolsmenu()

def l4menu():
	os.system('cls||clear')
	print(f"""
                  ╔═══════════════╗
	                ║     Layer4    ║
	╔═══════════════╩══════╦════════╩═══════════════╗
	║  Socket-TCP          ║  <empty>               ║
	║  UDP                 ║  <empty>               ║  
	║  TCP-SYN             ║  <empty>               ║
	║  Memcrashed          ║  <empty>               ║
	║  <empty>             ║  <empty>               ║
	╚══════════════════════╩════════════════════════╝
	""")
	try:
		while (True):
			layer4 = input(f"{c.green}[FireNet{rgb()}@{c.purple}Root]$>{rgb()} ")
			if layer4 == "Socket-TCP" or layer4 == "socket-tcp":
				call(["python3", "./files/sock.py"])
			elif layer4 == "home" or layer4 == "Home":
				main()
			elif layer4 == "UDP" or layer4 == "udp":
				call(["python3", "./files/udp.py"])
			elif layer4 == "TCP-SYN" or layer4 == "tcp-syn":
				call(["python3", "./files/syn.py"])
			elif layer4 == "Memcrashed" or layer4 == "memcrashed":
				call(["python3", "./files/mem.py"])
			else:
				print(":/ its not that hard to type.")
	except KeyboardInterrupt:
		l4menu()

def l7menu():
	os.system('cls||clear')
	print(f"""
	                ╔═══════════════╗
	                ║     Layer7    ║
	╔═══════════════╩══════╦════════╩═══════════════╗
	║  cf-captcha          ║  cf-uam                ║
	║  cfb                 ║  http-power            ║  
	║  http-raw            ║  .onion-slam           ║
	║  http-post           ║  <empty>               ║
	║  http-proxy          ║  <empty>               ║
	╚══════════════════════╩════════════════════════╝
	""")
	try:
		while (True):
			layer7 = input(f"{c.green}[FireNet{rgb()}@{c.purple}Root]$>{rgb()} ")
			if layer7 == "cf-captcha":
				call(["node", "./files/captcha.js"])
			elif layer7 == "cfb":
				print("NodeJS (1) or Python (2) Version of CF-Bypass")
				norp = input(">> ")
				if norp == "1":
					call(["node", "./files/cfb.js"])
				elif norp == "2":
					call(["node", "./files/cfbypass.py"])
				else:
					print("Are you dumb? select 1 or 2.")
			elif layer7 == "http-raw":
				call(["node", "./files/http.js"])
			elif layer7 == "http-post":
				call(["python3", "./files/post.py"])
			elif layer7 == "http-proxy":
				call(["python3", "./files/proxy.py"])
			elif layer7 == "cf-uam":
				call(["node", "./files/uam.py"])
			elif layer7 == "http-power":
				call(["python3", "./files/raw.py"])
			elif layer7 == ".onion-slam":
				call(["python3", "./files/tor.py"])
			elif layer7 == "home" or layer7 == "Home":
				main()
			else:
				print("Are you stupid? type it out correctly.")
	except KeyboardInterrupt:
		l7menu()
		

def main():
	os.system('cls||clear')
	print(f"""
	{rgb()}d88888b d888888b d8888b. d88888b d8b   db d88888b d888888b 
	{rgb()}88'       `88'   88  `8D 88'     888o  88 88'     `~~88~~' 
	{rgb()}88ooo      88    88oobY' 88ooooo 88V8o 88 88ooooo    88    
	{rgb()}88~~~      88    88`8b   88~~~~~ 88 V8o88 88~~~~~    88    
	{rgb()}88        .88.   88 `88. 88.     88  V888 88.        88    
	{rgb()}YP      Y888888P 88   YD Y88888P VP   V8P Y88888P    YP    
	{rgb()}
		                ╔═══════════════╗
		                ║     HOME      ║
		╔═══════════════╩══════╦════════╩═══════════════╗
		║  layer7              ║  tools                 ║
		║  layer4              ║  Info                  ║  
		╚══════════════════════╩════════════════════════╝
				 type 'home' to return back here.
																
																														 """)
	while (True):
		try:
			cmd = input(f"{c.green}[FireNet{rgb()}@{c.purple}Root]$>{rgb()} ")
			
			if cmd == "layer7" or cmd == "l7" or cmd == "Layer7":
				l7menu()
			elif cmd == "layer4" or cmd == "l4" or cmd ==  "Layer4":
				l4menu()
			elif cmd == "tools" or cmd == "Tools":
				toolsmenu()
			elif cmd == "home" or cmd == "Home":
				main()
			elif cmd == "exit" or cmd == "Exit":
				sys.exit()
			elif cmd == "Info" or cmd == "info":
				info()
			else:
				print("Are you sure your not stupid? type that again.")
		except KeyboardInterrupt:
			main()
		
try:
	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	main()
except Exception as e:
	print("An error occured:",e)
	time.sleep(5)
	main()