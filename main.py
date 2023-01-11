# -*- coding: utf-8 -*-

import os
import time
import sys


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
			tools = input(f"{c.green}[FireNet{c.black}@{c.purple}Root]$>{c.black} ")
			if tools == "resolver":
				os.system(f'python ./files/resolver.py')
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
	║  Spoof-TCP           ║  <empty>               ║
	║  UDP                 ║  <empty>               ║  
	║  TCP-SYN             ║  <empty>               ║
	║  <empty>             ║  <empty>               ║
	║  <empty>             ║  <empty>               ║
	╚══════════════════════╩════════════════════════╝
	""")
	try:
		while (True):
			layer4 = input(f"{c.green}[FireNet{c.black}@{c.purple}Root]$>{c.black} ")
			if layer4 == "Spoof-TCP":
				os.system(f'python ./files/sock.py')
			elif layer4 == "home" or layer4 == "Home":
				main()
			elif layer4 == "UDP" or layer4 == "udp":
				os.system(f'python ./files/udp.py')
			elif layer4 == "TCP-SYN" or layer4 == "tcp-syn":
				os.system(f'python ./files/syn.py')
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
			layer7 = input(f"{c.green}[FireNet{c.black}@{c.purple}Root]$>{c.black} ")
			if layer7 == "cf-captcha":
				os.system(f'node ./files/captcha.js')
			elif layer7 == "cfb":
				print("NodeJS (1) or Python (2) Version of CF-Bypass")
				norp = input(">> ")
				if norp == "1":
					os.system(f'node ./files/cfb.js')
				elif norp == "2":
					os.system(f'python ./files/cfbypass.py')
				else:
					print("Are you dumb? select 1 or 2.")
			elif layer7 == "http-raw":
				os.system(f'node ./files/http.js')
			elif layer7 == "http-post":
				os.system(f'python ./files/post.py')
			elif layer7 == "http-proxy":
				os.system(f'python ./files/proxy.py')
			elif layer7 == "cf-uam":
				os.system(f'node ./files/uam.js')
			elif layer7 == "http-power":
				os.system(f'python ./files/raw.py')
			elif layer7 == ".onion-slam":
				os.system(f'python ./files/tor.py')
			elif layer7 == "home" or layer7 == "Home":
				main()
			else:
				print("Are you stupid? type it out correctly.")
	except KeyboardInterrupt:
		l7menu()
		

def main():
	os.system('cls||clear')
	print(f"""
	{c.black}d88888b d888888b d8888b. d88888b d8b   db d88888b d888888b 
	{c.yellow}88'       `88'   88  `8D 88'     888o  88 88'     `~~88~~' 
	{c.orange}88ooo      88    88oobY' 88ooooo 88V8o 88 88ooooo    88    
	{c.red}88~~~      88    88`8b   88~~~~~ 88 V8o88 88~~~~~    88    
	{c.pink}88        .88.   88 `88. 88.     88  V888 88.        88    
	{c.orange}YP      Y888888P 88   YD Y88888P VP   V8P Y88888P    YP    
	{c.black}
		                ╔═══════════════╗
		                ║     HOME      ║
		╔═══════════════╩══════╦════════╩═══════════════╗
		║  layer7              ║  tools                 ║
		║  layer4              ║  <empty>               ║  
		╚══════════════════════╩════════════════════════╝
		     type 'home' to return back here.
																
																														 """)
	while (True):
		try:
			cmd = input(f"{c.green}[FireNet{c.black}@{c.purple}Root]$>{c.black} ")
			
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