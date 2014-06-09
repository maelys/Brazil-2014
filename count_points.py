#!/usr/bin/env python

import sqlite3

def main():

    winner = raw_input("Enter the winner of the Game: ")
    conn = ''
    cur = ''
    conn = sqlite3.connect('brazil2014.sqlite')
    cur = conn.cursor()

    group1=["Spain","Germany","Portugal","Brazil","Colombia","Uruguay","Argentina","Switzerland"]
    group2=["Italy","Greece","England","Belgium","Chile","USA","Netherlands","France"]
    group3=["Russia","Mexico","Croatia","IvoryCoast","Bosnia","Algeria","Ecuador","Honduras"]
    group4=["CostaRica","Iran","Ghana","Nigeria"]
    group5=["Japan","Cameroon","Korea","Australia"]

    #winner="Brazil"
    #winner="France"

    points_to_add=0

    if winner in group1:
        points_to_add=1
    elif winner in group2:
        points_to_add=2
    elif winner in group3:
        points_to_add=3
    elif winner in group4:
        points_to_add=5
    elif winner in group5:
        points_to_add=7
    else:
        print winner," is not in the DB"


    cur.execute("UPDATE contestants SET points=points+" + str(points_to_add) + " WHERE " + winner + " NOT LIKE 0;")
    conn.commit()
    cur.execute("SELECT name,points FROM contestants;")
    conn.commit()
    

if __name__ == '__main__':
    main()
