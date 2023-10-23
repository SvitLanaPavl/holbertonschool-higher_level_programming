#!/usr/bin/python3
'''takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument'''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    '''Lists all states from the database hbtn_0e_0_usa'''

    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    query = 'SELECT * FROM states WHERE name = %s ORDER BY id'
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()
    for state in states:
        print(state)
