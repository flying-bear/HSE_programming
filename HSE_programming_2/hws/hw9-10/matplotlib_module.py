##Необходимо:
##    взять словарь дотракийского языка: http://wiki.dothraki.org/Vocabulary;
##    посчитать число слов каждой части речи и визуализировать количество с помощью matplotlib;
##    посчитать число слов для каждой буквы (начинающихся на определённую букву) и визуализировать это количество.

import matplotlib.pyplot as plt
from matplotlib import style

def matplot(alpha, POS):
    style.use('ggplot')
    X = [1,   1.5, 2,   3, 5, 6]
    Y = [1.8, 1,   3.6, 2, 1, 3]

    dots = ['Первая', "Вторая", "Третья", "Четвертая", "Пятая", "Шестая"]

    for x, y, d in zip(X, Y, dots):
        plt.scatter(x, y, s=100)
        plt.text(x+0.1, y+0.1, d) # +0.1 - это чтобы текст не наползал на маркер, а отрисовывался чуть выше и правее 
    plt.show()
    plt.show()
    return True

def get_alphabet_and_POS(d): #dict of POS with words as keys
    alpha = {}
    POS = {}
    for key in d:
        if key[0] not in alpha:
            alpha[key[0]] = 1
        else:
            alpha[key[0]] += 1
        if d[key] not in POS:
            POS[d[key]] = 1
        else:
            POS[d[key]] += 1
    return alpha, POS
