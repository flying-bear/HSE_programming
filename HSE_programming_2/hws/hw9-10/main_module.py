##Необходимо:
##    взять словарь дотракийского языка: http://wiki.dothraki.org/Vocabulary;
##    посчитать число слов каждой части речи и визуализировать количество с помощью matplotlib;
##    посчитать число слов для каждой буквы (начинающихся на определённую букву) и визуализировать это количество.

from crawler_module import get_dict
from matplotlib_module import matplot, get_alphabet_and_POS

def main():
    d = get_dict()
    alpha, POS = get_alphabet_and_POS(d)
    matplot([alpha, POS])


if __name__ == '__main__':
    main()
