##TO DO:
##    stats page
##    search page
##    results page
##    move to SQL database

from flask import Flask
from flask import url_for, render_template, request, redirect

import json

from uuid import uuid4

app = Flask(__name__)

data = {}



@app.route('/')
def index(): #анкета с социологическими полями ---> записываться в файл
    urls = {'главная (эта страница - анкета с полями)': url_for('index'),
            'анкета социолингвистическими с полями': url_for('form'),
            'результаты в систематизированном виде': url_for('stats'),
            'json со всеми введенными на сайте данными': url_for('jsonify'),
            'поиск': url_for('search'),
            'результаты поиска (попадаем сюда только после поиска)': url_for('results')}
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_userdata():
    user_id = str(uuid4())
    userdata = {}
    userdata['userName'] = request.values['userName']
    userdata['userAge'] = request.values['userAge'],
    userdata['userSex'] = request.values['userSex'],
    userdata['userEducation'] = request.values['userEducation'],
    userdata['userYearsOfEducation'] = request.values['userYearsOfEducation'],
    userdata['userProfession'] = request.values['userProfession'],
    userdata['userBirthPlace'] = request.values['userBirthPlace'],
    userdata['userPlace'] = request.values['userPlace']
    data[user_id]['personal'] = userdata
    return redirect(url_for('form', uid=user_id))

@app.route('/form') #анкета с социолингвистическими полями ---> записываться в файл
def form():
    uid = request.args['uid']
    return render_template('form.html', uid=uid)

@app.route('/form', methods=['POST']) #анкета с социолингвистическими полями ---> записываться в файл
def process_form():
    answers = request.form
    uid = request.args['uid'] 
    data[uid]['answers'] = answers
    with open('results.json', 'a', encoding='utf-8') as f:
        json.dump(data[uid], f, ensure_ascii = False, indent = 4)
        f.write('\n,')
    return redirect(url_for('stats'))

@app.route('/stats') # результаты в систематизированном виде
def stats():
    number_of_participants = len(data)
    ... #compute something
    return render_template('stats.html')


@app.route('/json')
def jsonify(): # json со всеми введенными на сайте данными
    with open('results.json', 'r', encoding='utf-8') as f: ## перевести на БД
        jsontext = json.loads(f.read().strip(',') + ']')
    with open('templates/json.html', 'r', encoding='utf-8') as f:
        currenttexet = f.read()
        header = currenttexet.split('<span>')[0] + '<span>  '
        footer = ' </span>' + currenttexet.split('</span>')[-1]
    with open('templates/json.html', 'w', encoding='utf-8') as f:
        f.write(header + jsontext + footer)
    return render_template('json.html')

@app.route('/search')
def search(): # поиск
    ... #process search return redirect(url_for('results') parametrics = parametrics)
    return render_template('search.html')

@app.route('/results')
def results(): # результаты поиска
    if request.args:
        parametrics = request.args['parametrics']
        return render_template('results.html', parametrics=parametrics)
    return redirect(url_for('search'))

if __name__ == '__main__':
    app.run(debug=True)