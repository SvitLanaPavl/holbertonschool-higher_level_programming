#!/usr/bin/python3
'''takes in an argument and displays all cities
in the states table of hbtn_0e_0_usa where name
matches the argument safe from injections'''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    '''Lists all states from the database hbtn_0e_0_usa'''

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = '''SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC;
            '''
    cursor.execute(query)
    cities = cursor.fetchall()
    cities = [item[1] for item in cities if item[1] == argv[4]]
    print(', '.join(cities))
