import re


def getMeta(html): ## Вынимает из HTML имя автора, дату написания, URL, название статьи
    meta = ['', ## 0 -- имя автора, если его можно достать со страницы (и вообще если оно есть), -- находит кроме случаев, когда оно часть plain text новости
            '', ## 1 -- дата в формате 07.01.2012 (день.месяц.год)
            '', ## 2 -- URL, откуда статья была скачана
            ''] ## 3 -- название статьи
    regAuthorBox = re.compile('<a href="\/author\/\?id=\d*?" class="author-name font-open-s">(.*?)<\/a>.*?<p class="author-mail font-open-s">.*?Автор', re.DOTALL)
    regAuthorP = re.compile('<p>(.*?) <span style="text-transform: uppercase;">(.*?)<\/span><\/p>', re.DOTALL)
    regDate = re.compile('<p class="date font-open-s-light">(.*? ).*?<\/p>', re.DOTALL)
    regSource = re.compile('<span class="aa-block"><a href="(.*?)\?set-aa=normal" class="data-aa-off" data-aa-off>', re.DOTALL)
    regTitle = re.compile('<h1 class="news-title simple font-open-semibold">(.*?)<\/h1>', re.DOTALL)
    authorP = regAuthorP.search(html)
    authorB = regAuthorBox.search(html)
    date = regDate.search(html)
    source = regSource.search(html)
    title = regTitle.search(html)
    if authorP:
        meta[0] = authorP.group(1).strip() + ' ' + authorP.group(2).strip()
    elif authorB:
        meta[0] = authorB.group(1).strip()
    if date:
        meta[1] = date.group(1).strip()
    if source:
        meta[2] = 'https://ks-yanao.ru' + source.group(1).strip()
    if title:
        meta[3] = title.group(1).strip()
    return meta


def getPlainText(html): ## Вынимает из HTML текст статьи и чистит от тегов, лишних пробелов и переносов строк
    plainText = ''
    regArticle = re.compile('<div class="description font-open-s-light nm-b">(.*?)<div', re.DOTALL)
    regTag = re.compile('<.*?>', re.DOTALL)
    regLine = re.compile('\n(\s)*?\n', re.DOTALL)
    regSpace = re.compile('[\t ]{2,}', re.DOTALL)
    article = regArticle.search(html)
    if article:
        withoutTags = regTag.sub('', article.group(1))
        withoutHTMLSpaces = re.sub('&nbsp;', '', withoutTags)
        withoutAddSpaces = regSpace.sub(' ', withoutHTMLSpaces)
        plainText = regLine.sub('\n', withoutAddSpaces)
    return plainText


def main():
    pass
        

if __name__ == "__main__":
    main()
