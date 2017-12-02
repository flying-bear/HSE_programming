##TO DO:
##    stats page
##    search page
##    results page
##    move to SQL database

from flask import Flask
from flask import url_for, render_template, request, redirect

import json
import sqlite3

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
    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()
    user_id = str(uuid4())
    userdata = {}
    userdata['userName'] = request.values['userName']
    userdata['userAge'] = int(request.values['userAge'])
    userdata['userSex'] = request.values['userSex']
    userdata['userLanguage'] = request.values['userLanguage']
    userdata['userEducation'] = request.values['userEducation']
    userdata['userYearsOfEducation'] = int(request.values['userYearsOfEducation'])
    userdata['userProfession'] = request.values['userProfession']
    userdata['userBirthPlace'] = request.values['userBirthPlace']
    userdata['userPlace'] = request.values['userPlace']
    data[user_id] = {}
    data[user_id]['personal'] = userdata
    cur.execute('INSERT INTO users (uid, Name, Age, Sex, Language, Education, YearsOfEducation, Profession, BirthPlace, Place) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        [user_id, userdata['userName'], userdata['userAge'], userdata['userSex'], userdata['userLanguage'], userdata['userEducation'],
         userdata['userYearsOfEducation'], userdata['userProfession'], userdata['userBirthPlace'], userdata['userPlace']])
    conn.commit()
    return redirect(url_for('form', uid=user_id))

@app.route('/form') #анкета с социолингвистическими полями ---> записываться в файл
def form():
    uid = request.args['uid']
    return render_template('form.html', uid=uid)

@app.route('/form', methods=['POST']) #анкета с социолингвистическими полями ---> записываться в файл
def process_form():
    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()
    answers = request.form
    uid = request.args['uid']
    data[uid] = {}
    data[uid]['answers'] = answers
    for i in range(1, len(answers)):
        cur.execute('INSERT INTO answers (uid, qid, answer) Values(?, ?, ?)',
                    [uid, i, data[uid]['answers']['A'+str(i)]])
    conn.commit()
    return redirect(url_for('stats'))

@app.route('/stats') # результаты в систематизированном виде
def stats():
    ...
    return render_template('stats.html')


@app.route('/json')
def jsonify(): # json со всеми введенными на сайте данными
    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()
    jsontext = {}
    cur.execute('SELECT uid FROM users')
    uids = cur.fetchall()
    for urow in uids:
        u=''.join(urow[0])
        jsontext[u] = {}
        cur.execute('SELECT * FROM users WHERE uid=?', urow)
        user_data = cur.fetchone()
        jsontext[u]['personal'] = user_data
        cur.execute('SELECT * FROM answers WHERE uid=?', urow)
        user_answers = cur.fetchall()
        jsontext[u]['answers'] = user_answers
    jsoned = json.dumps(jsontext)
    return jsoned

@app.route('/search')
def search(): # поиск
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search(): # поиск
    ... #process search 
    return redirect(url_for('results'), parametrics = parametrics)

@app.route('/results')
def results(): # результаты поиска
    if request.args:
        parametrics = request.args['parametrics']
        return render_template('results.html', parametrics=parametrics)
    return redirect(url_for('search'))

if __name__ == '__main__':
    app.run(debug=True)
