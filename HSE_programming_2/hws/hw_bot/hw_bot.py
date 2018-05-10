##    Написать программу-бота, с которой можно разговаривать: пользователь пишет ей реплику, а она отвечает предложением,
##    в котором все слова заменены на какие-то случайные другие слова той же части речи и с теми же грамматическими характеристиками.
##    Предложение-ответ должно быть согласованным. Например, на фразу "Мама мыла раму" программа может ответить "Девочка пела песню".
##    Для такой программы вам понадобится большой список русских слов: можно взять список словоформ с сайта НКРЯ - http://ruscorpora.ru/corpora-freq.html
##    Из этого списка вам нужен только список разных лемм разных частей речи, и затем нужно будет использовать функции parse и inflect.

import json
import os
from random import choice
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()
dictionary = {}

def get_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def get_file_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def write_text_in_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    
def analyze(form):
    a = morph.parse(form)[0] ## Parse(word='любимая', tag=OpencorporaTag('ADJF,Subx,Qual femn,sing,nomn'), normal_form='любимый', 
                              ## score=0.666666, methods_stack=((<DictionaryAnalyzer>, 'любимая', 367, 7),))
    an = {}
    an['tag'] = str(a.tag)
    an['normal'] = str(a.normal_form)
    an['word'] = str(a.word)
    return an


def get_dictionary(lines):
    for line in lines:
        form = line.split()[-1].strip()
        analyzis = analyze(form)
        tag = analyzis['tag']
        normal = analyzis['normal']
        dictionary[form] = {'tag':tag, 'normal':normal}
    write_text_in_file('jsdict.json', json.dumps(dictionary, ensure_ascii = False))
               

def find_form(grammar, d, known_types):
    forms = []
    if grammar is not in known_types:
        for key in d:
            if grammar == d[key]['tag']:
                forms.append(key)
            known_types[grammar] = forms
    else:
        forms = known_types[grammar]
    if forms:
        random_form = choice(forms)
    else:
        random_form = 'form_not_found'
    write_text_in_file('know_types.txt', json.dunps(known_types))
    return random_form


def make_pseudorandom_phrase(phrase):
    words = phrase.split()
    new_phrase = ''
    for i in range(len(words)):
        word = words[i]
        g = analyze(word)['tag']
        if i == 0:
            new_phrase = find_form(g, dictionary).capitalize() + ' '
        elif i == len(words) - 1:
            new_phrase += find_form(g, dictionary)
        else:
            new_phrase += find_form(g, dictionary) + ' '
    return new_phrase


def main():
    if os.path.exists('jsdict.json'):
        dictionary = json.loads(get_file_text('jsdict.json'))
    else:
        lines = get_file_lines('dict.txt')
        get_dictionary(lines)
    phrase = input('Введите предложение.  ')
    print(make_pseudorandom_phrase(phrase))
    


if __name__ == '__main__':
    main()
