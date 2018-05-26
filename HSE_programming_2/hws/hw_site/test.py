def process_search(Place, questionNumber, userMinAge, userMaxAge): # поиск
    parametrics = {}
    parametrics['Place'] = Place
    parametrics['questionNumber'] = questionNumber
    parametrics['userMinAge'] = userMinAge
    parametrics['userMaxAge'] = userMaxAge
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
        if age[0]>user_data[3] or age[1]<user_data[3]:
            continue
        needed_users.append(urow)
   
    if not needed_users:
        needed_users = users

    answers = {}
    if not questionNumber:
        for urow in needed_users:
            cur.execute('SELECT * FROM answers WHERE uid=?', urow)
            answer = cur.fetchall()
            answers[urow] = answer
    else:
        for urow in needed_users:
            cur.execute('SELECT * FROM answers WHERE uid=? AND qid=?', (urow, questionNumber))
            answer = cur.fetchone()
            answers[urow] = answer
    return redirect(url_for('results', answers=answers))
