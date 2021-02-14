import re
import socket
import requests
import urllib2
import urllib
import os
import sys
import time
import cookielib
from bs4 import BeautifulSoup
from platform import system


banner =""" 
!-----------------!
!  xBING          !          
!      by         !           
!       pr3d80r   !       /n/
!-----------------!      /e/
(\-/)  '                /k/
(*v*) '                /o/
/   >'                /r/
--------------------- b/
"""
print (banner)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
print ("""
do you have dork list?(y/n)
""")

meh = raw_input("hum?  :")

class males():

	def Dorker(self):
		your = raw_input("Dorks list :  ")
		your = open(your, 'r')
		for hater in your:
			never = []
			ever = 1
			while ever < 900:
				BEmine = "http://www.bing.com/search?q="+hater+"&go=Search&count=50&first="+str(ever)+"&FORM=PERE"
				uDONT = requests.get(BEmine,verify=False,headers=headers)
				KILLme = uDONT.content
				peace = re.findall('<h2><a target="_blank" href="(.*?)"', KILLme)
				for i in peace:
					o = i.split('/')
					if (o[0]+'//'+o[2]) in never:
						pass
					else:
						never.append(o[0]+'//'+o[2])
						print '[>>]',(o[0]+'//'+o[2])
						with open('Random.txt', 'a') as s:
							s.writelines((o[0]+'//'+o[2])+'\n')
				ever = ever+50


broken = males()
if meh == 'y':
	broken.Dorker()
else:
	print("oka bye bussy")
	
#use this and make a better one
#i modified this,from mr spy bot
#t.me/th3b4g
