import requests

f = open('token.txt', 'r+')
f.truncate(0)
TOKEN = f.read()
f.close()


headers = {'User-Agent': 'MyBot/0.0.1', 'Authorization': "bearer " + TOKEN }

base_url = 'https://oauth.reddit.com'

res = requests.get(base_url + '/r/depression/comments/taofpm/nobody_believes_you_when_youre_highfunctioning/.json?limit=1', headers=headers)

res_json = res.json()[0]['data']['children'][0]['data']['selftext']

print(res.json())
