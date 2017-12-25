##TO DO:
##    search page
##        explanations
##    results page

from flask import Flask
from flask import url_for, render_template, request, redirect

import json
import sqlite3
import re

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
    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT uid FROM users')
    uids = cur.fetchall()
    for urow in uids:
        u=''.join(urow[0])
    uniq = []
    num = 0
    male = 0
    yearsum = 0
    yearofedsum = 0
    moved = 0
    uniq_place = []
    for urow in uids:
        u=''.join(urow[0])
        if u not in uniq:
            uniq.append(u)
            num += 1
            cur.execute('SELECT * FROM users WHERE uid=?', urow)
            user_data = cur.fetchall()[0]
            if 'male' in user_data:
                male += 1
            yearsum += user_data[3]
            yearofedsum += user_data[7]
            place = user_data[-1]
            if user_data[-2] != place:
                moved += 1
            if place not in uniq_place:
                uniq_place.append(place)
    n_places = len(uniq_place)
    places = sorted(uniq_place)
    places = ', '.join(places)
    percent_male = (male/num)*100
    average_age = yearsum/num
    average_years_of_ed = yearofedsum/num
    percent_moved = (moved/num)*100
    return render_template('stats.html', num=num, percent_male=percent_male, average_age=average_age, average_years_of_ed=average_years_of_ed,
                           percent_moved=percent_moved, n_places=n_places, places=places)


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

@app.route('/results')
def results(): # поиск
    parametrics = {}
    if request.values:
        parametrics['Place'] = request.values['Place']
        parametrics['questionNumber'] = request.values['questionNumber']
        parametrics['userMinAge'] = request.values['userMinAge']
        parametrics['userMaxAge'] = request.values['userMaxAge']
        conn = sqlite3.connect('data.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT uid FROM users')
        uids = cur.fetchall()

        questionNumber = 0
        if parametrics['questionNumber']:
            questionNumber = parametrics['questionNumber']

        age = [6,90]
        if parametrics['userMinAge']:
            age[0] = parametrics['userMinAge']
        if parametrics['userMaxAge']:
            age[1] = parametrics['userMaxAge']

        needed_users = []
        users = []
        for urow in uids:
            if urow not in users:
                users.append(urow)
            cur.execute('SELECT * FROM users WHERE uid=?', urow)
            user_data = cur.fetchall()[0]
            if parametrics['Place']:
                if parametrics['Place'] != user_data[-1]:
                    continue
            if int(age[0])>user_data[3] or int(age[1])<user_data[3]:
                continue
            needed_users.append(urow)
       
        if not needed_users:
            return redirect(url_for('search'))

        answers = {}
        if not questionNumber:
            for urow in needed_users:
                cur.execute('SELECT * FROM answers WHERE uid=?', urow)
                answer = cur.fetchall()
                answers[urow[0]] = answer
        else:
            for urow in needed_users:
                cur.execute('SELECT * FROM answers WHERE uid=? AND qid=?', (urow[0], questionNumber))
                answer = cur.fetchall()
                answers[urow[0]] = answer
##            return(str(answers))
        for key in answers:
            l = answers[key]
            n = []
            for a in l:
                n.append([a[1], a[2]])
            answers[key] = n
    return render_template('results.html', answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
