
import urllib.request
import json

req = urllib.request.Request('https://api.vk.com/method/users.get?user_ids=452804881&fields="has_photo,city,bdate,screen_name"&v=5.8&access_token=7edf36a87edf36a87edf36a8e97ebd1a9977edf7edf36a8241effefb17f20cb63fb17ab')
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
data = json.loads(result)
print(data['response'])


def get_new_user_info(user_id, ids):
    req = urllib.request.Request('https://api.vk.com/method/users.get?user_ids=' + str(user_id) + '&fields="has_photo,city,bdate,screen_name"&v=5.8&access_token=7edf36a87edf36a87edf36a8e97ebd1a9977edf7edf36a8241effefb17f20cb63fb17ab')
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
    ids[raw_post['from_id']] = {'age' : age, 'city' : city}
    return {'age' : age, 'city' : city}

ids = {}
raw_post = {}
raw_post['id'] = 2849
req = urllib.request.Request('https://api.vk.com/method/wall.getComments?owner_id=-60449041&post_id=' + str(raw_post['id']) + '&v=5.74&access_token=7edf36a87edf36a87edf36a8e97ebd1a9977edf7edf36a8241effefb17f20cb63fb17ab')
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
data = json.loads(result)
comments = {}
for item in data['response']['items']:
    if item['from_id'] not in ids:
        user_info = get_new_user_info(raw_post['from_id'], ids)
        age = user_info['age']
        city = user_info['city']
    else:
        age = ids[item['from_id']]['age']
        city = ids[item['from_id']]['city']
    comments[item['id']] = { 'text' : item['text'],
                             'n' : len(item['text'].replace('/n',' ').split()),
                             'author' :
                             { 'id' : item['from_id'],
                               'age' : age,
                               'city' : city}
                             }
print(comments[0])

##    {'from_id': 402898299, 'text': 'К сожалению уже не найду, но мне попадался текст какого-то христианина, который обосновывал концепцию «лучшего из миров»
##     тем фактом, что мы развиваем медицину, то есть боремся с болезнями, а значит нам очень нравится эта жизнь. Если бы нам не нравилась жизнь,
##     мы не стремились ее продлевать. Похоже, простая мысль, что в «лучшем из миров» мы бы не нуждались в лечении от тысяч заболеваний, каждое из которых
##     «мечтает» тебя прикончить, ему в голову не пришла.', 'id': 2862, 'date': 1518811039}
    
##    {'reply_to_user': 336089594, 'reply_to_comment': 2869, 'id': 2871, 'text': '[id336089594|Евгений], ох уж эти типичные идеалисты...',
##     'date': 1520675964, 'from_id': 452804881}
