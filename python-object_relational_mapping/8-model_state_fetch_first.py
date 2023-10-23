#!/usr/bin/python3
'''prints the first State object from the database hbtn_0e_6_usa'''
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print(f'{state.id}: {state.name}')
    else:
        print('Nothing')
