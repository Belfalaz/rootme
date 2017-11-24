from irc import *
import os, random, math

channel = "#root-me_challenge"
server = "irc.root-me.org"
nickname = "yawnling"
target = "Candy"

irc = IRC()
irc.connect(server, channel, nickname)

while 1:
	print("[+] Sending !ep1 to " + target)
	text = irc.get_text(target)
	print(text)
	try:
		stext = text.split(":")
		print("[+] Receive Message : " + stext[2])
		finaltext = stext[2].split(" / ")
		num1 = finaltext[0]
		num2 = finaltext[1]
		print("[+] Split to Number1 : " + num1)
		print("[+] Split to Number2 : " + num2)
		result = round(math.sqrt(int(num1)) * int(num2), 2)
		result = bytes(str(result).encode("ASCII"))
		print("[+] Result of sqrt " + num1 + " multiply " + num2 + " : " + result)
		print("[+] Sending Result to : " + target)
		ntext = irc.ans_text(target, result) 	#breakpoint
		print("[+] Receive Flag...")
		print(ntext)
		print("[+] Sending 'Bye Bye' 0/")
		irc.send("QUIT")
		break
	except:
		print("[!] Waiting for Message...")

irc.close()

