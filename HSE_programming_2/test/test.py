##    1. (5 баллов) Скачать отсюда архив страниц интернет-сайта с тайско-английским словарём. Извлечь с каждой страницы
##    пары "тайское слово -- английское слово" и поместить их в питоновскую структуру данных типа "словарь",
##    где ключом будет тайское слово, а значением - английское.
##
##    2. (8 балла) Использовать структуру данных из предыдущего задания, записать её в файл формата json на диск,
##    а также создать ещё одну структуру данных, где будет наоборот: английское слово ключ, а массив тайских слов - значение.
##    Её тоже записать на диск в формате json.
##
##    3. (10 баллов) Создать на фласке веб-приложение "Англо-тайский словарь", где можно было бы в текстовом поле ввести английское слово
##    и получить в качестве результата запроса - его перевод на тайский.

from bs4 import BeautifulSoup
import json
import os
import re

def get_dict(html):
    d = {}
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    tr_items = soup.find_all('tr')
    for it in tr_items:
        trs = it.find_all('td')
        if trs:
            w = trs[0].find('a')
            if w:
                w = w.get_text()
                d[w] = trs[-1].get_text()
    return d

def crawl():
    d = {}
    lst = os.listdir('thai_pages')
    for fl in lst:
        with open('thai_pages/'+fl, 'r', encoding='utf-8') as f:
            html = f.read()
            d.update(get_dict(html))
    return d #5

def jsonify(d):
    text = json.dumps(d)
    with open('thai-eng.json', 'w', encoding='utf-8') as f:
        f.write(text)
    inv_d = {v: k for k, v in d.items()}
    new_inv_d = {}
    for key in inv_d:
        if ';' in key:
            keys = key.split(';')
            for k in keys:
                new_inv_d[k] = inv_d[key]
        else:
            new_inv_d[key] = inv_d[key]
    inv_d.update(new_inv_d)
    text_i = json.dumps(inv_d)
    with open('eng-thai.json', 'w', encoding='utf-8') as f:
        f.write(text_i) #8

def main():
    d = crawl()
    jsonify(d)


if __name__ == '__main__':
    main()
