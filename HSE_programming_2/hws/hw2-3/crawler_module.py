import urllib.request
import re
import os

from cleaner_module import getPlainText
from meta_module import getMeta


def getPageHTML(url): ## по URL выдаёт HTML 
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return html


def getLinks(baseUrl): ## из base url (в данном случае - https://ks-yanao.ru/novosti/?PAGEN_2=) постранично ищет все ссылки на новости, выдаёт их списком
    links = []
    for n in range(1): ##502 is the last page
        pagelinks = []
        pageText = getPageHTML(baseUrl + str(n+1))
        regLink = re.compile('href=".*?" class="news-link text-none"')
        pageLinks = regLink.findall(pageText)
        for i in range(len(pageLinks)):
            pageLinks[i] = 'https://ks-yanao.ru' + pageLinks[i].split('"')[1]
            if pageLinks[i] not in links:
                links.append(pageLinks[i])
    return links


def crawl(baseurl):
    links = getLinks(baseurl)
    weirdlinks = []
    csv = 'path' + '\t' + 'author' + '\t' + 'sex' + '\t' + 'birthday' + '\t' + 'header' + '\t' + 'created' + '\t' + 'sphere' + '\t' + 'genre_fi' + '\t' + 'type' + '\t' + 'topic' + '\t' + 'chronotop' + '\t' + 'style' + '\t' + 'audience_age' + '\t' + 'audience_level' + '\t' + 'audience_size' + '\t' + 'source' + '\t' + 'publication' + '\t' + 'publ_year' + '\t' + 'medium' + '\t' + 'country' + '\t' + 'region' + '\t' + 'language'
    for link in links:
        html = getPageHTML(link)
        text = getPlainText(html)
        author, title, date, url = getMeta(html)
        if url != link:
            weirdlinks.append(url + ' - ' + link)
        if date:
            day, month, year = date.split('.')
            directory = os.path.join('Красный_север', 'plain', year, month)
        else:
            year = 'unknown year'
            date = 'unknown date'
            directory = os.path.join('unknown date')
        if not author:
            author = 'Noname'
        text = '@au ' + author + '\n@ti ' + title + '\n@da' + date + '\n@url ' + url + '\n' + text
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = re.sub('[./\?]', '', title)
        directory = os.path.join(directory, filename+'.txt')
        with open(directory, 'w', encoding = 'utf-8') as f:
                f.write(text)
        raw = '%s\t%s\t\t\t%s\t%s\tпублицистика\t\t\t\t\tнейтральный\tн-возраст\tн-уровень\tреспубликанская\t%s\tКрасный Север\t\t%s\tгазета\tРоссия\tЯмало-Ненецкий Административный Округ\tru'
        csv += raw % (directory, author, title, date, link, year)
    with open('weird links.txt', 'w', encoding = 'utf-8') as f:
        for link in weirdlinks:
            f.writeline(link)
    with open (os.path.join('Красный_север', 'metadata.csv'), 'w', encoding = 'utf-8') as f:
        f.write(csv)
    return True
