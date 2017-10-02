from crawler_module import crawl, getLinks
from mystem_module import mystem_xml, mystem_plain

def main():
##    getLinks('https://ks-yanao.ru/novosti/?PAGEN_2=')
    links = []
    with open('links.txt', 'r', encoding = 'utf-8') as f:
        links = f.readlines()
    crawl(links)
    print('done')

if __name__ == '__main__':
    main()
