#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from flask import (Flask, request, jsonify)
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest

import config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI;

db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.Boolean, nullable=False, default=False)
    q = db.Column(db.Text, nullable=False, default='')
    a = db.Column(db.Text, nullable=False, default='')
    cat = db.Column(db.String(255), nullable=False, default='')
    sort = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, q, a):
        self.deleted = False
        self.q = q
        self.a = a
        self.cat = ''
        self.sort = 0

    def to_json(self):
        return dict(id=self.id,
                deleted=self.deleted,
                q=self.q,
                a=self.a,
                cat=self.cat,
                sort=self.sort)


@app.route('/cards/')
def list_card():
    cards = Card.query.filter_by(deleted=False).all();
    return jsonify(result='ok', data=[c.to_json() for c in cards])

@app.route('/cards/<int:id>', methods=['DELETE'])
def del_card(id):
    card = Card.query.get_or_404(id)
    card.deleted = True
    db.session.add(card)
    db.session.commit()
    return jsonify(result='ok')

def validate_param_card(p):
    if not p.has_key('q'): raise BadRequest('Param q is required.')
    if p.get('q') == '': raise BadRequest('Param q is not allow empty.')
    if not p.has_key('a'): raise BadRequest('Param a is required.')

@app.route('/cards/<int:id>', methods=['PUT'])
def update_card(id):
    p = request.json
    validate_param_card(p)

    card = Card.query.get_or_404(id)
    card.q = p['q']
    card.a = p['a']
    db.session.add(card)
    db.session.commit()
    return jsonify(result='ok')

@app.route('/cards/', methods=['POST'])
def add_card():
    p = request.json
    validate_param_card(p)

    card = Card(p['q'], p['a'])
    db.session.add(card)
    db.session.commit()
    return jsonify(result='ok')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9092, debug=True)


