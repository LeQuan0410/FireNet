# -*- coding: utf-8 -*-
import requests
import os

os.system('cls||clear')

ip = input("IP/DOMAIN: ")

print("""
╔═╗╔═╗╔═╗╦╔═╗
║ ╦║╣ ║ ║║╠═╝
╚═╝╚═╝╚═╝╩╩  

""")
try:
		r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
		print(r.text)
except:
		print("[ API Error :( ]")


print("""
╦═╗╔═╗╦  ╦╔═╗╦═╗╔═╗╔═╗  ╦╔═╗
╠╦╝║╣ ╚╗╔╝║╣ ╠╦╝╚═╗║╣   ║╠═╝
╩╚═╚═╝ ╚╝ ╚═╝╩╚═╚═╝╚═╝  ╩╩  

""")
try:
		r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
		print(r.text)
except:
		print("[ API Error :( ]")





print("""
╔═╗╦ ╦╔╗ ╔╗╔╔═╗╔╦╗
╚═╗║ ║╠╩╗║║║║╣  ║ 
╚═╝╚═╝╚═╝╝╚╝╚═╝ ╩ 

""")
try:
		r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
		print(r.text)
except:
		print("[ API Error :( ]")



print("""
╔═╗╔═╗╦  ╦  ╔═╗╔═╗╦╔═╦ ╦╔═╗
╠═╣╚═╗║  ║  ║ ║║ ║╠╩╗║ ║╠═╝
╩ ╩╚═╝╩═╝╩═╝╚═╝╚═╝╩ ╩╚═╝╩  

""")
try:
		r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
		print(r.text)
except:
		print("[ API Error :( ]")



print("""
╔╦╗╔╗╔╔═╗  ╦  ╔═╗╔═╗╦╔═╦ ╦╔═╗
 ║║║║║╚═╗  ║  ║ ║║ ║╠╩╗║ ║╠═╝
═╩╝╝╚╝╚═╝  ╩═╝╚═╝╚═╝╩ ╩╚═╝╩  

""")
try:
		r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
		print(r.text)
except:
		print("[ API Error :( ]")



print("""
╦═╗╔═╗╦  ╦╔═╗╦═╗╔═╗╔═╗  ╔╦╗╔╗╔╔═╗
╠╦╝║╣ ╚╗╔╝║╣ ╠╦╝╚═╗║╣    ║║║║║╚═╗
╩╚═╚═╝ ╚╝ ╚═╝╩╚═╚═╝╚═╝  ═╩╝╝╚╝╚═╝

""")
try:
		r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
		print(r.text)
except:
		print("[ API Error :( ]")