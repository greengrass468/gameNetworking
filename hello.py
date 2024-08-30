# -*- coding: utf-8 -*-

from flask import Flask, abort, render_template
app = Flask(__name__)
 
@app.route('/')
def hello():
    return 'MI-PYT je nejlepší předmět na FITu!'

#~ @app.route('/en') pokud nedám na konec / tak funguje jen /en
@app.route('/en/') #/en/ -> funguje /en a /en/
def hello_en():
    return 'MI-PYT is the best class at FIT!'

@app.route('/user/<username>/')
def username(username):
    return 'User: {}'.format(username)

@app.route('/user/<username>/cz')
def username_cz(username):
    return 'Uživatel: {}'.format(username)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello2(name=None):
    return render_template('hello.html', name=name)
 
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
