import re

def getMeta(html): ## Вынимает из HTML имя автора, дату написания, URL, название статьи
    print('getting meta')
    meta = ['', ## 0 -- имя автора, если его можно достать со страницы (и вообще если оно есть), -- находит кроме случаев, когда оно часть plain text новости
            '', ## 1 -- название статьи
            '', ## 2 -- дата в формате 07.01.2012 (день.месяц.год)
            ''] ## 3 -- URL, откуда статья была скачана
    regAuthorBox = re.compile('<a href="\/author\/\?id=\d*?" class="author-name font-open-s">(.*?)<\/a>.*?<p class="author-mail font-open-s">.*?Автор', re.DOTALL)
    regAuthorP = re.compile('<p>(.*?) <span style="text-transform: uppercase;">(.*?)<\/span><\/p>', re.DOTALL) 
    regTitle = re.compile('<h1 class="news-title simple font-open-semibold">(.*?)<\/h1>', re.DOTALL)
    regDate = re.compile('<p class="date font-open-s-light">(.*? ).*?<\/p>', re.DOTALL)
    regSource = re.compile('<span class="aa-block"><a href="(.*?)\?set-aa=normal" class="data-aa-off" data-aa-off>', re.DOTALL)
    authorP = regAuthorP.search(html)
    authorB = regAuthorBox.search(html)
    title = regTitle.search(html)
    date = regDate.search(html)
    source = regSource.search(html)
    if authorP:
        meta[0] = authorP.group(1).strip() + ' ' + authorP.group(2).strip()
    elif authorB:
        meta[0] = authorB.group(1).strip()
    if title:
        meta[1] = title.group(1).strip()
    if date:
        meta[2] = date.group(1).strip()
    if source:
        meta[3] = 'https://ks-yanao.ru' + source.group(1).strip()
    return meta

