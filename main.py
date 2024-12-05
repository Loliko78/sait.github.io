import random
import g4f
import requests
import sqlite3
from threading import Thread
from flask import Flask, request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')

"""@app.route('/add', methods=['POST', 'GET'])
def helo_world():
  if request.method == "POST":
        title = request.form['Title']
        about = request.form['About']
        url_site = request.form['Url_site']
        pay = request.form['Pay']"""


@app.route('/all', methods=['POST', 'GET'])
def helo_world():

  q = request.args.get('q')
  print(q)
  if q!='Одежда' and q!='ПК' and q!='Услуги' and q!='Игры' and q!='Другое' and q:
    connection = sqlite3.connect('min.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE art = ?', (q,))
    import random
    tables = cursor.fetchall()
    return render_template('all.html', data=tables)
  elif q=='Одежда':
    connection = sqlite3.connect('min.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE kat = ?', (q,))
    import random
    tables = cursor.fetchall()
    random.shuffle(tables)
    return render_template('all.html', data=tables)
  elif q=='ПК':
    connection = sqlite3.connect('min.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE kat = ?', (q,))
    import random
    tables = cursor.fetchall()
    random.shuffle(tables)
    return render_template('all.html', data=tables)
  elif q=='Услуги':
    connection = sqlite3.connect('min.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE kat = ?', (q,))
    import random
    tables = cursor.fetchall()
    random.shuffle(tables)
    return render_template('all.html', data=tables)
  elif q=='Игры':
    connection = sqlite3.connect('min.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE kat = ?', (q,))
    import random
    tables = cursor.fetchall()
    random.shuffle(tables)
    return render_template('all.html', data=tables)
  elif q=='Другое':
    connection = sqlite3.connect('min.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE kat = ?', (q,))
    import random
    tables = cursor.fetchall()
    random.shuffle(tables)
    return render_template('all.html', data=tables)
  else:
    connection = sqlite3.connect('min.db')
    cursor = connection.cursor()
    cursor.execute("""select * from Users""")
    import random
    tables = cursor.fetchall()

    random.shuffle(tables)

  return render_template('all.html', data=tables)

def run():
  app.run(host='0.0.0.0', port=8080)

def start():
  t = Thread(target=run)
  t.start()

