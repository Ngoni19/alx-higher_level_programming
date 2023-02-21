#!/usr/bin/python3
"""
Script-->state create "California" with city attribute "San Francisco"
params: username, password & database
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
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

    # state create "California" having attri "San Francisco"
    NewS = State(name="California")
    NewC = City(name="San Francisco")
    NewS.cities.append(NewC)

    session.add(NewS)
    session.add(NewC)

    session.commit()
    session.close()
