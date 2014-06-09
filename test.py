#!/usr/bin/env python

import sqlite3
import collections
import jinja2

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
    #return render_template('index.html',results=od)
    return jinja2.Template(open('template.html').read()).render(results=od)


open('/home/emc/public_html/wc/index.html', 'w').write(display_results())

