from bs4 import BeautifulSoup
import re
import urllib.request

def get_weather():
    attempts = 5
    while attempts:
        try:
            req = urllib.request.Request('https://weather.com/weather/today/l/42.00,21.43')
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
                c = re.search('<span class="">(.*?)<sup>', html).group(1)
                p = re.search('class="today_nowcard-phrase">(.*?)<', html).group(1)
                weather = c + '°C, ' + p
            break
        except ConnectionResetError or TimeoutError :
            print('the connection lost, was not able to reconnect, I wait for 30sec')
            time.sleep(30)
            attempts -=1
    if not attempts:
        print('I ran out of attempts limit')
        weather = 'uncnown'
    return weather

def get_top10(d):
    values = d.values()
    top=[]
    for i in range (10):
        maxim=max(values)
        for k, v in d.items():
            if v == maxim:
                if k not in top:
                    top.append(k)
                    d.pop(k)
                break
        values.remove(maxim)
    return top

def get_nplus():
    attempts = 5
    while attempts:
        try:
            req = urllib.request.Request('https://nplus1.ru/')
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
                soup = BeautifulSoup(html, 'html.parser')
                text = soup.get_text()
                rus = re.findall('[А-ЯЁа-яё ]{2,}', text)
                drus = {}
                for w in rus:
                    w = w.strip()
                    if w:
                        if w not in drus:
                            drus[w] = 1
                        else:
                            drus[w] += 1
                top = get_top10(drus)
                rus = ' '.join(drus.keys())
            break
        except ConnectionResetError or TimeoutError :
            print('the connection lost, was not able to reconnect, I wait for 30sec')
            time.sleep(30)
            rus = []
            attempts -=1
    if not attempts:
        print('I ran out of attempts limit')
        rus = []
    return rus, top

def get_dict_inks():
    attempts = 5
    while attempts:
        try:
            req = urllib.request.Request('http://www.dorev.ru/ru-index.html?l=c0')
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('Windows-1251')
                soup = BeautifulSoup(html, 'html.parser')
                text = soup.get_text()
                links = []
                link_items = soup.find_all('a')
                for a in link_items:
                    links.append(a.get('href'))
                letter_links = []
                for link in links:
                    if link:
                        if 'ru-index.html?l=' in link:
                            letter_links.append(link)
                d = set(letter_links)
            break
        except ConnectionResetError or TimeoutError :
            print('the connection lost, was not able to reconnect, I wait for 30sec')
            time.sleep(30)
            attempts -=1
    if not attempts:
        print('I ran out of attempts limit')
        d = set()
    return d

