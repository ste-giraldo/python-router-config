#!/usr/bin/python

import sys
import time
import paramiko 
import getpass
import os
import cmd

#Comment or decommend lines in static or prompted authentication to use preferred auth mode
#Static authentication
#USER = ''
#PASSWD = ''
#SECRET = ''
#End Static authentication

#Prompted authentication
USER = raw_input("Username: ")
PASSWD = getpass.getpass("Password: ")
print ('If your device does not use an enable password, just press Enter')
SECRET = getpass.getpass("Enable Password: ")
#End Prompted authentication

#start FOR ...in 
#open host list from file
f = open('host_file')
for ip in f.readlines():
	ip = ip.strip()
	#session start
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username=USER, password=PASSWD)
	#ssh shell
	chan = client.invoke_shell()
	time.sleep(0.5)
	#enter enable secret
	chan.send('enable\n')
	time.sleep(0.5)
	chan.send(SECRET +'\n')
	#open commands list from file
	f = open('config_file')
        for command in f.readlines():
	  chan.send (command)
          time.sleep(0.5)
	output = chan.recv(99999999)
	#show output config and write file
	print output
	ff = open('logfile.txt', 'a')
	ff.write(output)
	ff.close()
	#close ssh session
	client.close() 
	
	print ip
	f.close()
