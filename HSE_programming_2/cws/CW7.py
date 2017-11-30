import sqlite3

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()
##cur.execute('CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, surname VARCHAR, age INTEGER)') # создать таблицу
cur.execute('INSERT INTO data (name, surname, age) VALUES (?, ?, ?)',['Andrew', 'Lloyd', 25]) #запрос SQL: добавить запись
cur.execute('INSERT INTO data (name, surname, age) VALUES (?, ?, ?)',['Pauline', 'Henriette', 25])
##res = cur.fetchone() #лист
cur.execute('UPDATE data set age=24  WHERE name="Andrew"') #изменить запись
##cur.execute('DELETE FROM data WHERE id = 2') #удалить записи
cur.execute('SELECT name, surname FROM data WHERE age >= 20') #найти все записи
res = cur.fetchall() #лист кортежей
cur.execute('SELECT avg(age) FROM data') #найти все записи
res = cur.fetchall()
print(res)
conn.commit() #сохранить изменения
