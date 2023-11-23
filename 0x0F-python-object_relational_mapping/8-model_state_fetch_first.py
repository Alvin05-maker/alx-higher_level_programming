#!usr/bin/python3
"""
print the first State object
"""


import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    firstInstance = query(States).first()
    if firstInstance is None:
        print("Nothing")
    else:
        print('{}: {}'.format(firstInstance.id, firstInstance.name))
