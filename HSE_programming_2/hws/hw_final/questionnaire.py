from flask import Flask
from flask import url_for, render_template, request, redirect

import json
from random import choice as choose


app = Flask(__name__)

data = {}

def choose_puzzle(puzzles):
    puzzle = choose(puzzles)
    return puzzle

def check_answer(given, answer, puzzle): ## puzzle - массив слов из загадки
    if given == answer:
        puzzle = choose_puzzle(puzzles)
        return ['Правильно!', puzzle]
    else:
        return ['Неправильно! Попробуйте ещё.', puzzle]

@app.route('/')
def index(): #главная страница
    urls = {'главная': url_for('index')}
    if request.args:
        answer = request.args.get('answer')
        puzzle = request.args.get('puzzle')
        if answer != "":
            response = check_answer(answer, puzzle)
    else:
        puzzle = create_puzzle()
    return render_template('index.html', response = response[0], puzzle = response[1])

if __name__ == '__main__':
    app.run(debug=True)
