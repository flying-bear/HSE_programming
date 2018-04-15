import json
import urllib.request  
##req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-150145347&count=100&v=5.73&access_token=7edf36a87edf36a87edf36a8e97ebd1a9977edf7edf36a8241effefb17f20cb63fb17ab') 
##response = urllib.request.urlopen(req)
##result = response.read().decode('utf-8')
##data = json.loads(result)
##for item in data['response']['items']:
##    print(item['text'])


req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-150145347&count=100&v=5.73&access_token=7edf36a87edf36a87edf36a8e97ebd1a9977edf7edf36a8241effefb17f20cb63fb17ab')
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
data = json.loads(result)
post_items = data['response']['items']
post_ids = []
for item in post_items:
    post_ids.append(item['id'])

commentors = {}
for post_id in post_ids:
    req = urllib.request.Request('https://api.vk.com/method/wall.getComments?owner_id=-150145347&post_id={}&extended=1&v=5.73&access_token=7edf36a87edf36a87edf36a8e97ebd1a9977edf7edf36a8241effefb17f20cb63fb17ab'.format(post_id)) 
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result)
    print(data)
    for person in data['response']['profiles']:
        if person['last_name']+ ' ' + person['first_name'] not in commentors:
            commentors[person['last_name']+ ' ' + person['first_name']] = 1
        else:
            commentors[person['last_name']+ ' ' + person['first_name']] += 1
    for group in data['response']['groups']:
        if group['name'] + ' ' + str(group['id']) not in commentors:
            commentors[group['name'] + ' ' + str(group['id'])] = 1
        else:
            commentors[group['name'] + ' ' + str(group['id'])] += 1
print(commentors)
# ломается на ссаных смайлах
