#!/usr/bin/python3
"""A script that deletes State objects with a name containing the letter a"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for cit in session.query(State, City).join(City).order_by(City.id):
        print("{:}: ({:}) {:}".format(cit[0].name, cit[1].id, cit[1].name))
    session.commit()
    session.close()
