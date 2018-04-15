## Программа должна уметь скачивать со стены больше, чем 100 постов, и больше, чем 100 комментариев к посту
## (если их действительно больше 100).
## Посчитайте питоном длину каждого поста и каждого комментария в словах.
## Создайте график, описывающий, как длина поста соотносится со средней длиной комментариев.
## Помимо выкачивания постов и комментариев, программа должна смотреть в профиль пользователя,
## который написал пост или сделал комментарий, и узнавать о нём социолингвистическую информацию:
## возраст и город (если они указаны). Для города достаточно id (то есть название узнавать не обязательно,
## хотя это можно сделать средствами API, а возраст нужно уметь вычислять.
##        Для каждого возраста нужно вычислить
##              - среднюю длину поста и комментария,
##              - нарисовать график, отражающий эту информацию.
##        Аналогичные графики нужно нарисовать для каждого города.
## Выложить скачанные тексты (тексты, как и в случае с газетным корпусом, нужно выкладывать не на github, а в репозитории дать ссылку),
##                                                                   построенные графики и сам код.


##posts =
## {post_id :
##         { 'text' : text,
##           'n' : number_of_words_in_post,
##           'author' :
##               { 'id' : author_id,
##                 'age' : author_age,
##                 'city' : author_city
##                   }
##           'comments':
##               [ {comment_id :
##                      { 'text' : text,
##                        'n' : number_of_words_in_comment,
##                        'author' :
##                            { 'id' : comment_author_id,
##                              'age' : comment_author_age,
##                              'city' : comment_author_city
##                               }
##                        }
##                    },
##                 {-||-}
##                   ]
##             }
##     }

##json.dump(dict, file, ensure_ascii = False)


import urllib.request
import json
import matplotlib.pyplot as plt

off = 0
end = 10000
raw_posts = []
while off < end:
    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-60449041&v=5.73&offset=' + str(off) + '&access_token=7edf36a87edf36a87edf36a8e97ebd1a9977edf7edf36a8241effefb17f20cb63fb17ab')
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result)
    if off == 0:
        end = data['response']['count']
    raw_posts = raw_posts + list(data['response']['items'])
    off += 100

posts = {}
for raw_post in raw_posts:
    req = urllib.request.Request('https://api.vk.com/method/users.get?user_ids=' + str(raw_post['from_id']) + '&fields="has_photo,city,bdate,screen_name"&v=5.8&access_token=7edf36a87edf36a87edf36a8e97ebd1a9977edf7edf36a8241effefb17f20cb63fb17ab')
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result)
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
    posts[raw_post['id']] = { 'text' : raw_post['text'],
                              'n' : len(raw_post['text'].replace('\n',' ').split()),
                              'author' : { 'id' : raw_post['from_id'], 'age' : age, 'city' : city}
                              'comments' : []}
