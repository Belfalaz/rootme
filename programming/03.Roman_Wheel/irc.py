import socket, sys

class IRC:

	s = socket.socket()

	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#def send(self, chan, msg):
	#self.s.send("PRIVMSG " + chan + " " + msg + "\r\n")

	def connect(self, server, chan, botnick):
		print("[+] Connecting to : " + server)
		try:
			self.s.connect((server, 6667))
		except:
			print("[!] Can't Connect to : " + server)
		else:
			print("[+] Sending Nickname Command")
			self.s.send("NICK " + botnick + "\r\n")
			print("[+] Sending USER Command")
			self.s.send("USER yawnling irc.root-me.org root-me :yawnling")
			print("[+] Joining Channel : " + chan)
			self.s.send("JOIN " + chan + "\r\n")

	def get_text(self, target):
		self.s.send("PRIVMSG " + target + " !ep3" + "\r\n")
		text = self.s.recv(7000)
		return text

	def ans_text(self, target, ans):
		self.s.send("PRIVMSG " + target + " !ep3 -rep " + ans + "\r\n")
		ftext = self.s.recv(7000)
		return ftext
