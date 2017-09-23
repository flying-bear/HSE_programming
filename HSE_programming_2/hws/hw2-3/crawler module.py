import urllib.request
import re


def getPageText(url): ## по URL выдаёт HTML 
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return html


def getLinks(baseUrl): ## из base url (в данном случае - https://ks-yanao.ru/novosti/?PAGEN_2=) постранично ищет все ссылки на новости, выдаёт их списком
    links = []
    for n in range(2): ##502
        pagelinks = []
        pageText = getPageText(baseUrl + str(n+1))
        regLink = re.compile('href=".*?" class="news-link text-none"')
        pageLinks = regLink.findall(pageText)
        for i in range(len(pageLinks)):
            pageLinks[i] = 'https://ks-yanao.ru' + pageLinks[i].split('"')[1] 
        links += pageLinks
    return links



def main():
    pass
        

if __name__ == "__main__":
    main()
