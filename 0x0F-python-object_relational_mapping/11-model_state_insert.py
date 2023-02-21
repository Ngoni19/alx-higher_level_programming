#!/usr/bin/python3
"""
Script--> state update: given id & state name
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # session add new state & commit to state table
    new = State(name="Louisiana")
    session.add(new)
    session.commit()

    print("{:d}".format(new.id))

    session.close()
