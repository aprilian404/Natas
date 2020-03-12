import requests

URL = "http://natas27.natas.labs.overthewire.org/index.php"
usr = "natas27"
passwd = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"

_data = {"username":"natas28", "password":""}

res = requests.post(url = URL, auth=(usr,passwd), data=_data)

print(res.content)
