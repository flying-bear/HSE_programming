## С помощью urllib.request нужно скачать главную страницу газеты,
## извлечь оттуда все заголовки статей и напечатать заголовки в отдельный текстовый файл.
import urllib.request
import re


def main():
    req = urllib.request.Request('https://ks-yanao.ru/')
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    regTitle = re.compile('<p class="(?:thumb-title|news-title news-titles) font-open-semibold">.*?</p>', flags= re.DOTALL)
    titles = regTitle.findall(html)
    clean_titles = []
    regTag = re.compile('<.*?>', re.DOTALL)
    regSpace = re.compile('\s{2,}', re.DOTALL)
    for t in titles:
        clean_t = regSpace.sub("", t)
        clean_t = regTag.sub("", clean_t)
        if clean_t not in clean_titles:
            clean_titles.append(clean_t)
    with open('titles.txt', 'w', encoding = 'utf-8') as f:
        for t in clean_titles:
            f.write(t+'\n')
        

if __name__ == "__main__":
    main()
