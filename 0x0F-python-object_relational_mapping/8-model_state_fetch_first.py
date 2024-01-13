#!/usr/bin/python3

"""
lists all State objects from the database hbtn_0e_6_usa
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

    first = session.query(State).order_by(State.id).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()
