#!/usr/bin/env python
import sqlite3

def main():
    conn = ''
    cur = ''
    conn = sqlite3.connect('brazil2014.sqlite')
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS contestants (id integer PRIMARY KEY AUTOINCREMENT,name TEXT,points INTEGER DEFAULT 0,\
        Spain INTEGER DEFAULT 0,Germany INTEGER DEFAULT 0,Portugal INTEGER DEFAULT 0,Brazil INTEGER DEFAULT 0,Colombia INTEGER DEFAULT 0,\
        Uruguay INTEGER DEFAULT 0,Argentina INTEGER DEFAULT 0,Switzerland INTEGER DEFAULT 0,Italy INTEGER DEFAULT 0,Greece INTEGER DEFAULT 0,\
        England INTEGER DEFAULT 0,Belgium INTEGER DEFAULT 0,Chile INTEGER DEFAULT 0,USA INTEGER DEFAULT 0,Netherlands INTEGER DEFAULT 0,\
        France INTEGER DEFAULT 0,Russia INTEGER DEFAULT 0,Mexico INTEGER DEFAULT 0,Croatia INTEGER DEFAULT 0,IvoryCoast INTEGER DEFAULT 0,\
        Bosnia INTEGER DEFAULT 0,Algeria INTEGER DEFAULT 0,Ecuador INTEGER DEFAULT 0,Honduras INTEGER DEFAULT 0,CostaRica INTEGER DEFAULT 0,\
        Iran INTEGER DEFAULT 0,Ghana INTEGER DEFAULT 0,Nigeria INTEGER DEFAULT 0,Japan INTEGER DEFAULT 0,Cameroon INTEGER DEFAULT 0,\
        Korea INTEGER DEFAULT 0,Australia INTEGER DEFAULT 0);")
    conn.commit() 
    f = open('teams_choice','r')
    i=0
    dict_people={}
    teams=[]
    name=''
    for line in f:
        line = line.rstrip('\n')
        if i%10==0:
            name=line
        if i%10==9:
            teams=[]
        if i%10==8:
            dict_people[name] = teams
        if (i%10!=0 and i%10!=9):
            teams.append(line)
        i=i+1
    #print dict_people

    insert_query = "INSERT INTO contestants (name) VALUES (?);"
    for key in dict_people.keys():
        name = "\"" + str(key)+ "\""
        cur.execute("INSERT INTO contestants (name) VALUES ("+name+");") 
        conn.commit()

    for key,values in dict_people.items():
        name = "\"" + str(key)+ "\""
        #print values[5]
        cur.execute("UPDATE contestants SET " + values[0] + " = 1, " + values[1] + " = 1, " + values[2] + " = 1, " + values[3] + " = 1, " + values[4] + " = 1, " + values[5] + " = 1, " + values[6] + " = 1, " + values[7] + " = 1 WHERE name = " + name + ";")
        conn.commit()

    #cur.execute("SELECT* FROM contestants WHERE ;")
    #for row in cur:
     #   print row

if __name__ == "__main__":
    main()
