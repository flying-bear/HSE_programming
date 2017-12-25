##    3. (10 баллов) Создать на фласке веб-приложение "Англо-тайский словарь", где можно было бы в текстовом поле ввести английское слово
##    и получить в качестве результата запроса - его перевод на тайский.

from flask import Flask
from flask import url_for, render_template, request, redirect
import json



app = Flask(__name__)

with open('eng-thai.json', 'r', encoding='utf-8') as f:
    d = json.loads(f.read())


@app.route('/')
def index(): 
        return render_template('index.html')

@app.route('/results')
def results(): # поиск
    if request.values:
        q = request.values['q']
        if q in d.keys():
            answer = d[q]
        else:
            answer = 'Sorry, but nothing was found!'
    else:
        return redirect(url_for('index'))
    return render_template('results.html', answer=answer) #10


if __name__ == '__main__':
    app.run(debug=True)
