#!/usr/bin/python3
'''lists all State objects from the database hbtn_0e_6_usa'''
from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(f'mysql+msqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print(f'{state.id}: {state.name}')
