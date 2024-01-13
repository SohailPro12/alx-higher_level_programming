#!/usr/bin/python3

"""
changes the name of a State object from the database hbtn_0e_6_usa
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

    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
    print(a_state.id)
    session.close()
