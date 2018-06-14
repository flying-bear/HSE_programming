from flask import Flask
from flask import url_for, render_template, request, redirect

import json
from random import choice as choose
from uuid import uuid4

app = Flask(__name__)

first = True
data = {}

def get_puzzles():
    with open('puzzles.json', 'r', encoding='utf-8') as f:
        puzzles = json.loads(f.read())
    return puzzles


puzzles = get_puzzles()


def choose_puzzle(puzzles):
    puzzle_a = choose(puzzles)
    return puzzle_a


def check(given, puzzle_a): ## puzzle_a - [[массив слов из загадки], ответ]
    if given == puzzle_a[1]:
        puzzle_a = choose_puzzle(puzzles)
        return ['Правильно!', puzzle_a]
    else:
        return ['Неправильно! Попробуйте ещё.', puzzle_a]


@app.route('/')
def index(): #главная страница
    puzzle_a = choose_puzzle(puzzles)
    response = ['', puzzle_a]
    user_id = str(uuid4())
    data[user_id] = response     
    return render_template('index.html', response = response[0], puzzle = ', '.join(response[1][0]), uid=user_id)

@app.route('/', methods=['POST'])
def process_ans():
    if 'answer' in request.form and 'uid' in request.form:
        answer = request.form['answer'].strip().lower()
        uid = request.form['uid']
        if answer:
            puzzle_a = data[uid][1]
            response = check(answer, puzzle_a)
            data[uid] = response
        else:
            response = data[uid]
    return render_template('index.html', response = response[0], puzzle = ', '.join(response[1][0]), uid=uid)

if __name__ == '__main__':
    app.run(debug=True)
