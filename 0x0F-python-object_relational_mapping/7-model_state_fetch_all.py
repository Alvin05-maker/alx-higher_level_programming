#!/usr/bin/python3
"""
List state objects from a database
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    my_session = Session()
    for state in my_session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
