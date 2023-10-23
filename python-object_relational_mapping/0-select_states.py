#!/usr/bin/python3
'''The module documentation'''
import MySQLdb


def list_states(username, password, database):
    '''Lists all states from the database hbtn_0e_0_usa
    
    Args:
    username: MySQL username
    password: MySQL password
    database: the databse name

    Return: list of tuple, in each: id and name
    '''
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute('SELECT id, name FROM states ORDER BY id ASC')
    states = cursor.fetchall()
    cursor.close()
    db.close()
    return states
