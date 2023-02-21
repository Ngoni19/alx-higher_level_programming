#!/usr/bin/python3
"""
Script--> return state id|state name
params: username, password, database & state name to match
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

    # database state id--python query given state name
    state = session.query(State).filter_by(name=argv[4]).first()
    if state:
        print("{:d}".format(state.id))
    else:
        print("Not found")
    session.close()
