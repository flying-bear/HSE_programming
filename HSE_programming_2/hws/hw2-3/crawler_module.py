import urllib.request
import re
import os
import time

from cleaner_module import getPlainText
from meta_module import getMeta
from mystem_module import mystem_xml, mystem_plain


def getPageHTML(url): ## по URL выдаёт HTML
    print('getting HTML')
    attempts = 5
    while attempts:
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
            break
        except ConnectionResetError or TimeoutError :
            print('the connection lost, was not able to reconnect, I wait for 30sec')
            time.sleep(30)
            html = ''
            attempts -=1
        except urllib.error.HTTPError or urllib.error.URLError:
            print('url error in ' + url)
            html = ''
    if not attempts:
        print('I ran out of attempts limit')
        html = ''
    return html

def getLinks(baseUrl): ## из base url (в данном случае - https://ks-yanao.ru/novosti/?PAGEN_2=) постранично ищет все ссылки на новости, выдаёт их списком
    links = []
    for n in range(1, 502): ##502 is the last page
        pagelinks = []
        pageText = getPageHTML(baseUrl + str(n))
        print('page ' + str(n) + ' of links in process')
        regLink = re.compile('href=".*?" class="news-link text-none"')
        pageLinks = regLink.findall(pageText)
        for i in range(len(pageLinks)):
            pageLinks[i] = 'https://ks-yanao.ru' + pageLinks[i].split('"')[1]
            if pageLinks[i] not in links:
                links.append(pageLinks[i])
        with open('links.txt', 'w', encoding = 'utf-8') as f:
            f.writelines(links)
    return links


def crawl(links):
    wordstotal = 0
    weirdlinks = []
    csv = 'path' + '\t' + 'author' + '\t' + 'sex' + '\t' + 'birthday' + '\t' + 'header' + '\t' + 'created' + '\t' + 'sphere' + '\t' + 'genre_fi' + '\t' + 'type' + '\t' + 'topic' + '\t' + 'chronotop' + '\t' + 'style' + '\t' + 'audience_age' + '\t' + 'audience_level' + '\t' + 'audience_size' + '\t' + 'source' + '\t' + 'publication' + '\t' + 'publ_year' + '\t' + 'medium' + '\t' + 'country' + '\t' + 'region' + '\t' + 'language'
    i = 0
    for link in links:
        if wordstotal >= 150000:
            break
        i += 1
        print('article ' + str(i) + ' in process:')
        html = getPageHTML(link)
        text = getPlainText(html)
        wordstotal += len(text.split(' '))
        print("wrds in total:" + wordstotal)
        author, title, date, url = getMeta(html)
        if url != link:
            weirdlinks.append(url + ' - ' + link)
        if date:
            day, month, year = date.split('.')
            dateFolder = os.path.join(year, month)
            directory = os.path.join('ks-yanao', 'plain', dateFolder)
        else:
            year = 'unknown year'
            date = 'unknown date'
            directory = os.path.join('unknown date')
        if not author:
            author = 'Noname'
        text = '@au ' + author + '\n@ti ' + title + '\n@da' + date + '\n@url ' + url + '\n' + text
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = 'article' + str(i)
        plain_directory = os.path.join("ks-yanao", "mystem-plain", dateFolder)
        if not os.path.exists(plain_directory):
            os.makedirs(plain_directory)
            print(plain_directory + ' created')
        xml_directory = os.path.join("ks-yanao", "mystem-xml", dateFolder)
        if not os.path.exists(xml_directory):
            os.makedirs(xml_directory)
            print(xml_directory + ' created')
        mystem_xml(dateFolder, filename+'.txt')
        mystem_plain(dateFolder, filename+'.txt')
        directory = os.path.join(directory, filename+'.txt')
        with open(directory, 'w', encoding = 'utf-8') as f:
                f.write(text)
        raw = '%s\t%s\t\t\t%s\t%s\tпублицистика\t\t\t\t\tнейтральный\tн-возраст\tн-уровень\tреспубликанская\t%s\tКрасный Север\t\t%s\tгазета\tРоссия\tЯмало-Ненецкий Административный Округ\tru'
        csv += raw % (directory, author, title, date, link, year)
    with open('weird links.txt', 'w', encoding = 'utf-8') as f:
        for link in weirdlinks:
            f.write(link)
    with open (os.path.join('ks-yanao', 'metadata.csv'), 'w', encoding = 'utf-8') as f:
        f.write(csv)
    return links
