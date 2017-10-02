import re


def getPlainText(html): ## Вынимает из HTML текст статьи и чистит от тегов, лишних пробелов и переносов строк
    print('getting plain text')
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
