from irc import *
import os, random, base64

channel = "#root-me_challenge"
server = "irc.root-me.org"
nickname = "yawnling"
target = "Candy"

irc = IRC()
irc.connect(server, channel, nickname)

while 1:
	print("[+] Sending !ep2 to " + target)
	text = irc.get_text(target)
	print(text)
	try:
		stext = text.split(":")
		print("[+] Receive Message : " + stext[2])
		finaltext = stext[2]
		result = base64.b64decode(finaltext)
		result = bytes(result.encode("ASCII"))
		print("[+] Result of base64 decoded : " + result)
		print("[+] Sending Result to : " + target)
		ntext = irc.ans_text(target, result)
		print("[+] Receive Flag...")
		print(ntext)
		print("[+] Sending 'Bye Bye' 0/")
		irc.send("QUIT")
		break
	except:
		print("[!] Waiting for Message...")

irc.close()

