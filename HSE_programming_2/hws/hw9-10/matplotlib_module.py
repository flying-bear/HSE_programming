##Необходимо:
##    взять словарь дотракийского языка: http://wiki.dothraki.org/Vocabulary;
##    посчитать число слов каждой части речи и визуализировать количество с помощью matplotlib;
##    посчитать число слов для каждой буквы (начинающихся на определённую букву) и визуализировать это количество.

import matplotlib.pyplot as plt
from matplotlib import style

def matplot(l): #list of dicts
    fig, ax = plt.subplots(nrows=len(l), ncols=1)
    names = []
    X = []
    Y = []
    for i in range(len(l)):
        names.append([])
        X.append([])
        Y.append([])
        j = 0
        d = l[i]
        for key in d:
            j += 3
            names[i].append(key)
            X[i].append(j)
            Y[i].append(d[key])
        plt.subplot(2, 2, i+1)
        for x, y, d in zip(X[i], Y[i], names[i]):
            plt.scatter(x, y, s=20)
            plt.text(x+0.1, y+0.1, d) # +0.1 - это чтобы текст не наползал на маркер, а отрисовывался чуть выше и правее
    plt.show()

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
