import urllib.request
import json

offsets = [0, 1000, 2000, 3000, 4000]
users = []
for off in offsets:
    req = urllib.request.Request('https://api.vk.com/method/groups.getMembers?group_id=150145347&fields=city&v=5.73&offset=' + str(off) + '&access_token=7edf36a87edf36a87edf36a8e97ebd1a9977edf7edf36a8241effefb17f20cb63fb17ab')
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')   
    data = json.loads(result) 
    users = users + list(data['response']['items'])

cities = []
i = 0
for user in users:
    try:
        cities.append(user['city']['title'])
    except:
        pass

cities = [city for city in cities if city != '']
from collections import Counter
cities = Counter(cities)

import matplotlib.pyplot as plt

city_nums = [cities[city] for city in cities]
city_labs = [city for city in cities]
plt.bar(range(len(city_labs)), city_nums)

plt.title('Города в НМЖ')
plt.ylabel('Количество студентов')
plt.xlabel('Город')
plt.xticks(range(len(city_labs)), city_labs, rotation=90)
plt.legend()
plt.show()
