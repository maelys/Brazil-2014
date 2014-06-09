#!/usr/bin/env python

from flask import Flask,render_template, request
import re
import urllib2
from flask.ext.wtf import Form, BooleanField
import sqlite3
import collections

SECRET_KEY = 'tutu'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/create/')
def create_db():
    conn = ''
    conn = sqlite3.connect('wc.sqlite')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contestants (name TEXT,points INTEGER)")

    return render_template('index.html',"en construction")

@app.route('/')
def display_results():
    conn = ''
    conn = sqlite3.connect('brazil2014.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT name,points FROM contestants ORDER BY points DESC;")
    results={}
    while True:
        row=cur.fetchone()
        if row==None:
            break
        name=row[0]
        points=row[1]
        results[name]=points
    od = collections.OrderedDict(sorted(results.items(), key=lambda t: t[1],reverse=True))
    return render_template('index.html',results=od)


if __name__ == '__main__':
    app.run(debug=True)
