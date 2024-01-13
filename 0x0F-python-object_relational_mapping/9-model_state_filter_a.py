#!/usr/bin/python3

"""
lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from model_state import Base, State
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, password, db_name, pool_pre_ping=True))
    Base.metadata.create_all(engine)

    session = Session(engine)

    results = session.query(State).filter(State.name.like(
                            "%a%")).order_by(State.id).all()
    for state in results:
        print("{}: {}".format(state.id, state.name))
    session.close()
