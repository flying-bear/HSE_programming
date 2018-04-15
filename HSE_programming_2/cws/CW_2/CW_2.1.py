## В той же группе скачать 1000 записей со стены.
## Нарисовать график, показывающий, сколько записей было написано в каждый час.
## Вывести записи, набравшие наибольшее количество лайков и с наибольшим числом комментариев.

import urllib.request
import json
import datetime
import matplotlib.pyplot as plt

offsets = range(0,1000,100)
posts = []
for off in offsets:
    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-142260873&v=5.73&offset=' + str(off) + '&access_token=7edf36a87edf36a87edf36a8e97ebd1a9977edf7edf36a8241effefb17f20cb63fb17ab')
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result) 
    posts = posts + list(data['response']['items'])

print(data)
print(posts[0])

hours = {i:0 for i in range(24)}
most_liked = [0,0]
most_commented = [0,0]
for i in range(len(posts)):
    post = posts[i]
    hour = datetime.datetime.fromtimestamp(int(post['date'])).hour
    hours[hour] += 1
    if post['likes']['count'] > most_liked[0]:
        most_liked = [post['likes']['count'], post['text']]
    if post['comments']['count'] > most_commented[0]:
        most_commented = [post['comments']['count'], post['text']]

print("most liked post: \n" + most_liked[1])
print("most commented post: \n" + most_commented[1])

hour_nums = [hours[hour] for hour in hours]
hour_labs = [hour for hour in hours]
plt.bar(range(len(hour_labs)), hour_nums)

plt.title('Посты по часам')
plt.ylabel('Количество постов')
plt.xlabel('Время')
plt.xticks(range(len(hour_labs)), hour_labs)
plt.legend()
plt.show()
