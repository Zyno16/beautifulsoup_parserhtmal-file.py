import urllib.request, urllib.parser, urllib.error
import bs4 import BeautifulSoup
import ssl
# ssl secure sockets layer from hacker
# ignore ssl certifiate errors 
ctx = ssl.create_default_context()
ctx.ckeck_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter _')
html = urllib.request.urlopen(url, context=ctx).read()
soup  = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href',None)) 
