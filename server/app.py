#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import (Flask, request, session, g, redirect,
                   url_for, render_template, flash,
                   send_from_directory, abort,
                   render_template, flash, send_from_directory,
                   render_template_string)
import json

from flask_mysqldb import MySQL
import config

app = Flask(__name__)

app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB
app.config['MYSQL_HOST'] = config.MYSQL_HOST

mysql = MySQL(app)


@app.before_request
def setup_db():
    app.con = mysql.connection
    app.cur = mysql.connection.cursor()

@app.route('/cards/')
def list_card():
    app.cur.execute('''SELECT id, q, a, cat FROM cards''')
    items = []
    for item in app.cur.fetchall():
        items.append({
            'id': item[0],
            'q': item[1],
            'a': item[2],
            'cat': item[3]
            })
    return json.dumps({'result':'ok', 'data':items})

@app.route('/cards/<int:id>', methods=['DELETE'])
def del_card(id):
    app.cur.execute('''DELETE FROM cards WHERE id = %s;''', (id,))
    app.con.commit()
    return json.dumps({'result':'ok', 'data': ''})

def _get_param(req):
    id = req.form.get('id')
    q = req.form.get('q')
    a = req.form.get('a')
    cat = req.form.get('cat')
    if id is None and q is None and a is None and cat is None:
        d = json.loads(req.data)
        id = d.get('id')
        q = d.get('q')
        a = d.get('a')
        cat = d.get('cat')
        if id is None and q is None and a is None and cat is None:
            return None
    return {
        'id': id,
        'q': q,
        'a': a,
        'cat': cat
    }

@app.route('/cards/<int:id>', methods=['PUT'])
def update_card(id):
    p = _get_param(request)
    if p is None:
        return json.dumps({'result':'ng', 'data': 'Invalid parameters'})

    app.cur.execute(
        '''UPDATE cards SET q = %s, a = %s WHERE id = %s;''',
        (p['q'], p['a'], id)
        )
    app.con.commit()
    return json.dumps({'result':'ok', 'data': ''})

@app.route('/cards/', methods=['POST'])
def add_card():
    p = _get_param(request)
    if p is None:
        return json.dumps({'result':'ng', 'data': 'Invalid parameters'})
    app.cur.execute('''INSERT INTO cards(q, a) values(%s, %s);''', (p['q'], p['a']))
    app.con.commit()
    return json.dumps({'result':'ok', 'data': ''})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9092, debug=True)


