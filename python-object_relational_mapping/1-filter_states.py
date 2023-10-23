#!/usr/bin/python3
'''The module documentation: lists all states from
the database hbtn_0e_0_usa starting with N'''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    '''Lists all states from the database hbtn_0e_0_usa'''

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%")
    states = cursor.fetchall()
    for state in states:
        print(state)