#!/usr/bin/python3
"""list the first State object from a the state schema"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    _state = session.query(State).order_by(State.id).first()
    if _state is not None:
        print("{}: {}".format(_state.id, _state.name))
    else:
        print("Nothing")
    session.close()
