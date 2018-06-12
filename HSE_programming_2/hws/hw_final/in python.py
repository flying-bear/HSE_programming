##    программа играет с пользователем в игру "найди лишнее".
##    Программа загадывает программе несколько слов (минимум 4), пользователь сообщает в ответ, какое из этих слов является лишним в ряду.

import json
from random import choice as choose


def get_puzzles():
    with open('puzzles.json', 'r', encoding='utf-8') as f:
        puzzles = json.loads(f.read())
    return puzzles


def choose_puzzle(puzzles):
    puzzle_a = choose(puzzles)
    return puzzle_a

def check(given, puzzle_a): ##puzzle - массив слов из загадки
    if given == puzzle_a[1]:
        puzzle_a = choose_puzzle(puzzles)
        return ['Правильно!', puzzle_a]
    else:
        return ['Неправильно! Попробуйте ещё.', puzzle_a]

def main():
    global puzzles
    puzzles = get_puzzles()
    puzzle_a = choose_puzzle(puzzles)
    puzzle = puzzle_a[0]
    given = input('Выберите лишнее: ' + ', '.join(puzzle) + '. Ваш ответ: ')
    while given:
        result = check(given, puzzle_a)
        puzzle_a = result[1]
        puzzle = puzzle_a[0]
        print(result[0])
        given = input('Выберите лишнее: ' + ', '.join(puzzle) + '. Ваш ответ: ')
    print('Спасибо за игру!')

if __name__ == '__main__':
    main()
