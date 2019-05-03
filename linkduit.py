"""curl 'http://linkduit.mobi/user/dashboard' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://linkduit.mobi/user/dashboard' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Connection: keep-alive' -H 'Cookie: __cfduid=db7a88a8887b6198bf05b08aecf8b7cc31556855994; PHPSESSID=uij485q9v79k6p2v3590889315' -H 'Upgrade-Insecure-Requests: 1' --data 'url=babi.com'"""

"""curl 'http://linkduit.mobi/user/login' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://linkduit.mobi/user/login' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Alt-Used: linkduit.mobi:443' -H 'Connection: keep-alive' -H 'Cookie: __cfduid=db7a88a8887b6198bf05b08aecf8b7cc31556855994; PHPSESSID=uij485q9v79k6p2v3590889315' -H 'Upgrade-Insecure-Requests: 1' -H 'TE: Trailers' --data 'user_email=zekkelganteng%40gmail.com&user_pwd=serizawa"""

import requests
from requests import get, post, session
import re
import sys
import os

R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
C = '\033[36m' # cyan

def banner():
	print ("""
 _      ____  ____   __  _  ___    __ __  ____  ______ 
| |    |    ||    \ |  |/ ]|   \  |  |  ||    ||      |
| |     |  | |  _  ||  ' / |    \ |  |  | |  | |      |
| |___  |  | |  |  ||    \ |  D  ||  |  | |  | |_|  |_|
|     | |  | |  |  ||     \|     ||  :  | |  |   |  |  
|     | |  | |  |  ||  .  ||     ||     | |  |   |  |  
|_____||____||__|__||__|\_||_____| \__,_||____|  |__| 

CODED BY : KyuRazz ~ Family Attack Cyber

""")


class KyuRazz:
	def __init__(self):
		self.username = input("Email => ")
		self.password = input("Password => ")
		self.url = input("URL => ")
		self.header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/65.0',
					   'Cookie':'__cfduid=db7a88a8887b6198bf05b…ID=uij485q9v79k6p2v3590889315',
					   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
		self.login = ('http://linkduit.mobi/user/login')
		self.dashboard = ('http://linkduit.mobi/user/dashboard')
	def Serizawa(self):
		s = requests.Session()
		dataLogin = {'user_email':self.username,'user_pwd':self.password}
		masuk = s.post(self.login, data=dataLogin)
		kan = re.findall(r'	<h3 style="color: #404142;">(.*?)</h3>', masuk.text)
		print ("========/\========")
		print ("\033[32m[\033[36m*\033[32m] {}" .format(kan))
		link = {'url':self.url}
		upgan = s.post(self.dashboard, data=link)
		play = re.findall(r'<input onclick="this.select();" type="text" value="(.*?)">', upgan.text)
		kutaranai = s.get('http://linkduit.mobi/user/mylink')	
		zzz = re.findall(r'<a href="(.*?)">(.*?)</a>', kutaranai.text)
		kentel = (zzz[2])	
		print ("\033[32m[\033[36m*\033[32m] Your Short Link => {}" .format(kentel))
"""<a href="https://linkduit.net/4txus">https://linkduit.net/4txus</a>"""

if __name__ == "__main__":
	os.system('clear')
	banner()
	kyu = KyuRazz()
	kyu.Serizawa()
