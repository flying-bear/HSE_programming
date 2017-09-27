import os
from crawler_module import crawl
from mystem_module import mystem_xml, mystem_plain

def main():
    if crawl('https://ks-yanao.ru/novosti/?PAGEN_2='):
        print('downloaded')
    mystem_xml(os.join('Красный север','plain'))
    mystem_plain(os.join('Красный север','plain'))
    print('done')

if __name__ == '__main__':
    main()
