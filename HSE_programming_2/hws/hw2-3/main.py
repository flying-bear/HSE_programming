from crawler_module import crawl
from mystem_module import mystem_xml, mystem_plain

def main():
    crawl('https://ks-yanao.ru/novosti/?PAGEN_2=')
    print('downloaded')
    mystem_xml(r'C:\My\studies\HSE\programming\HSE_programming_2\hws\hw2-3\ks-yanao\plain\2017\09')
    mystem_plain(r'C:\My\studies\HSE\programming\HSE_programming_2\hws\hw2-3\ks-yanao\plain\2017\09')
    print('done')

if __name__ == '__main__':
    main()
