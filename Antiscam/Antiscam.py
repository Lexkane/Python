import requests 
import os
import random
import string
import json

chars=string.ascii_letters+string.digits+'!@#$%^&*()'
random.seed=(os.urandom(1024))

url='http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhs'

names=json.loads(open('names.json').read())

for name in names:
    name_extra=''.join(random.choice(string.digits))
    username=name.lower()+name_extra+'@yahoo.com'
    password=''.joiin(random.choice(chars)for i in range(8))

   requests.post(url,allow_redirects=False,data={ 
       'auid2ujauysd2uasdasdasd':username
    'kjauysd6sAJSDhyu12yasd':password })
   print (f'sending username {username} and password {password}')
    