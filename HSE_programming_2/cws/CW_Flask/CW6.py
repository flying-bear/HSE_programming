from flask import Flask, request, render_template
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    sufferings = ['being forever alone', 'endless friendzone', 'living in Russia', 'being a linguist']
    punishment = choice(sufferings)
    return render_template('main.html', punishment=punishment)

@app.route('/steal')
def steal():
    name = request.args['name']
    with open('data.txt', 'a', encoding = 'utf-8') as f:
        f.write(name)
    return "<h3>Now I've stolen your soul!<h3>"

@app.route('/hi')
def hi():
    if 'name' in request.args:
        name = request.args['name']
        return '<html><body><h1>Hi, {}!</h1></body></html>'.format(name)
    else:
        return '<html><body><h1>Type in your name</h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True)
