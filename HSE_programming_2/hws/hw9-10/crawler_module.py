##Необходимо:
##    взять словарь дотракийского языка: http://wiki.dothraki.org/Vocabulary;
##    посчитать число слов каждой части речи и визуализировать количество с помощью matplotlib;
##    посчитать число слов для каждой буквы (начинающихся на определённую букву) и визуализировать это количество.

from bs4 import BeautifulSoup
import re
import urllib.request

def get_dict():
    attempts = 5
    while attempts:
        try:
            req = urllib.request.Request('http://wiki.dothraki.org/Vocabulary', headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
                soup = BeautifulSoup(html, 'html.parser')
                text = soup.get_text()
                ul_items = soup.find_all('ul')
                new_ul_items = []
                for i in range(len(ul_items)):
                    ul_items[i] = ul_items[i].find('b')
                    if ul_items[i]:
                        word = ul_items[i].get_text()
                        new_ul_items.append(word)
                ul_items = new_ul_items   
                dl_items = soup.find_all('dl')
                for i in range(len(dl_items)):
                   dl_items[i] = dl_items[i].find('i')
                   if dl_items[i]:
                       dl_items[i] = dl_items[i].get_text()
                ul_dict = dict(zip(ul_items, dl_items))
            break
        except ConnectionResetError or TimeoutError :
            print('the connection lost, was not able to reconnect, I wait for 30sec')
            time.sleep(30)
            attempts -=1
    if not attempts:
        print('I ran out of attempts limit')
    return ul_dict
