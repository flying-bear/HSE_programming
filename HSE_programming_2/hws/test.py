
import urllib.request
import json

req = urllib.request.Request('https://api.vk.com/method/users.get?user_ids=12345&fields="has_photo,city,bdate,screen_name"&v=5.8&access_token=7edf36a87edf36a87edf36a8e97ebd1a9977edf7edf36a8241effefb17f20cb63fb17ab')
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
data = json.loads(result)
print(data['response'])
if 'city' in data['response'][0]:
    city = data['response'][0]['city']['title']
else:
    city = 'unknown'
if 'bdate' in data['response'][0]:
    if len(data['response'][0]['bdate']) > 5:
        age = 2018 - int(data['response'][0]['bdate'][4:])
    else:
        age = 'unknown'
else:
    age = 'unknown'
print('city = ' + city + ', age = ' + str(age))
