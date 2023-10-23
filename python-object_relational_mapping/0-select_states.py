#!/usr/bin/python3
'''The module documentation: lists all states from
the database hbtn_0e_0_usa'''
import MySQLdb
from sys import argv


if __name__ == 'main':
    '''Lists all states from the database hbtn_0e_0_usa'''

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
