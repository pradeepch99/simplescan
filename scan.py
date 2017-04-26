#!/usr/bin/python

#Author Pradeepch99

import requests
#ANSI colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


def request(domain,n):
	try:
		domain1=requests.get(domain, timeout=5)
		statuscode=domain1.status_code
		if statuscode==405 or statuscode==200:
			print(bcolors.FAIL+"%s - %d"+bcolors.ENDC)%(domain,statuscode)
			request.num=n+1
		else:
#			print("%s - %d")%(domain,statuscode)
			request.num=n
	except Exception as e:
#		print("%s looks not reachable"%(domain))
		request.num=n
		pass
	#print("n=== %s")%n

extns=('/','/Admin','/admin','/Administrator','/administrator','/phpmyadmin','/phpinfo','/phpinfo.php','/info.php','/.svn/entries','/wp-admin','/.htaccess','/.DS_Store','/wp-config.php','/config.php','/config','/backup','/backup.sql','/uploads','/upload','/upload.php','/uploads.php','/include','/includes','/~jbloggs','/wp-json/wp/v2/users/','/xmlrpc.php','/crossdomain.xml',':8080')


file = open('subdomain.txt', 'r')
for url in file:
	#print ("url "+url)
	url1=url.rstrip('\r\n')
	#print("url1 "+url1)
	n=0
	print(bcolors.OKGREEN+"[+] scanning site %s"+bcolors.ENDC)%url1
	for extns1 in extns:
		url2=str("http://"+url1+extns1)
		request(url2,n)
		n=request.num
		#print("num of extn %s")%n
		if n==29:
			print(bcolors.OKBLUE+"This might be a false positive"+bcolors.ENDC)