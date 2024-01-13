#!/usr/bin/python3

"""
 prints the State object with the name passed as argument
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
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, password, db_name, pool_pre_ping=True))
    Base.metadata.create_all(engine)

    session = Session(engine)

    results = session.query(State).filter(
            State.name == state_name).order_by(State.id).first()
    if results:
        print(results.id)
    else:
        print("Not found")
    session.close()
