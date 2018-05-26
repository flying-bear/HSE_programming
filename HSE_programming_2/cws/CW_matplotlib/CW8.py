##отдельно деревни, разным цветом пол, разным цветом разные гласны, по осям форманты

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

with open('nanai-vowels.csv', 'r', encoding='utf-8') as f:
    rows = f.readlines()
    header = rows[0].split(';')
    m1 = {'i' : {'x':[], 'y':[]}, 'I' : {'x':[], 'y':[]},  'e' : {'x':[], 'y':[]}}
    m2 = {'i' : {'x':[], 'y':[]}, 'I' : {'x':[], 'y':[]},  'e' : {'x':[], 'y':[]}}
    f1 = {'i' : {'x':[], 'y':[]}, 'I' : {'x':[], 'y':[]},  'e' : {'x':[], 'y':[]}}
    f2 = {'i' : {'x':[], 'y':[]}, 'I' : {'x':[], 'y':[]},  'e' : {'x':[], 'y':[]}}
    for row in rows[:-1]:
        row = row.split(';')
        if row[1] == 'm':
            if row[2] == 'Dzhuen':
                if row[3] == 'i':
                    m1['i']['x'] = row[4]
                    m1['i']['y'] = row[5]
                elif row[3] == 'I':
                    m1['I']['x'] = row[4]
                    m1['I']['y'] = row[5]
                else:
                    m1['e']['x'] = row[4]
                    m1['e']['y'] = row[5]
            else:
                if row[3] == 'i':
                    m2['i']['x'] = row[4]
                    m2['i']['y'] = row[5]
                elif row[3] == 'I':
                    m2['I']['x'] = row[4]
                    m2['I']['y'] = row[5]
                else:
                    m2['e']['x'] = row[4]
                    m2['e']['y'] = row[5]
        else:
            if row[2] == 'Dzhuen':
                if row[3] == 'i':
                    f1['i']['x'] = row[4]
                    f1['i']['y'] = row[5]
                elif row[3] == 'I':
                    f1['I']['x'] = row[4]
                    f1['I']['y'] = row[5]
                else:
                    f1['e']['x'] = row[4]
                    f1['e']['y'] = row[5]
            else:
                if row[3] == 'i':
                    f2['i']['x'] = row[4]
                    f2['i']['y'] = row[5]
                elif row[3] == 'I':
                    f2['I']['x'] = row[4]
                    f2['I']['y'] = row[5]
                else:
                    f2['e']['x'] = row[4]
                    f2['e']['y'] = row[5]
        
coord = [[m1, f1],[m2, f2]]
colors = ['blue', 'plum']
markers = ['s','o','^']
fig, ax = plt.subplots(nrows=1, ncols=2)

names = ['Dzhuen', 'Naikhin']

for row in ax:
    for col, name, coor in row, names, coord:
        col.title(name)
        col.xlabel('formant 1')
        col.ylabel('formant 2')
        for sex, color in coor, colors:
            for key, marker in sex, markers:
                col.scatter(coor[sex][key]['x'], coor[sex][key]['y'], c=color, marker = marker, label = key)
        col.legend()


plt.show()
