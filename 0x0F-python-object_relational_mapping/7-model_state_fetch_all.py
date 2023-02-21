#!/usr/bin/python3
"""
Script--> return all state objects from database with python
params: username, password & database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # database engine
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # database - query 
    for instance in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(instance.id, instance.name))

    session.close()
