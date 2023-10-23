#!/usr/bin/python3
'''takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument'''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    '''Lists all states from the database hbtn_0e_0_usa'''

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = 'SELECT * FROM states WHERE name = {:s}'.format(argv[4])
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
