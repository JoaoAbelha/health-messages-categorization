secret = '_i_HGBtmTqfRiafuV_zmQs0WrCvk7w'
import pandas as pd


import requests

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('ZlfxzjyaLsA9B4jiVK01BA', secret)

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'Bee31099',
        'password': 'boris1999'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

print(res.json())
# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

f = open('token.txt', 'a')
f.write(TOKEN)
f.close()

print("Token updated")

'''
# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

'''