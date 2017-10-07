import json
import urllib.request


def get_data(user):
    url = 'https://api.github.com/users/%s/repos' % user
    response = urllib.request.urlopen(url)  # посылаем серверу запрос и достаем ответ
    text = response.read().decode('utf-8')  # читаем ответ в строку
    data = json.loads(text) # превращаем джейсон-строку в объекты питона
    return data


def get_langs(data):
    langs = {}
    for i in data:
        if i['language']:
            if i['language'] not in langs:
                langs[i['language']] = 1
            else:
                langs[i['language']] += 1
    return langs


def get_max(dictionary):
    i = 0
    for Key in sorted(dictionary, key=dictionary.get, reverse=True):
        i += 1
        max_dict = Key + ': ' + str(dictionary[Key])
        if i = 1:
            break
    return max_dict

def main():
    users = ['elmiram', 'nevmenandr', 'shwars', 'JelteF', 'timgraham', 'arogozhnikov', 'accommodavid', 'jasny', 'bcongdon', 'whyisjake']
    languages = {}
    amonut = {}
    for user in users:
        data = get_data(user)
        amount[user] = len(data)
        user_langs = get_langs(data)
        for lang in user_langs:
            if lang in languages:
                languages[lang] += user_langs[lang]
            else:
                languages[lang] = user_langs[lang]
    print(get_max(languages))
    print(get_max(amount))
            

if __name__ == '__main__':
    main()
