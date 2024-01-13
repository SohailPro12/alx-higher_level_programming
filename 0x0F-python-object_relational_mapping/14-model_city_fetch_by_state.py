#!/usr/bin/python3

"""
prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from model_state import Base, State
    import sys
    from model_city import City
    from sqlalchemy.schema import Table

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, password, db_name, pool_pre_ping=True))
    Base.metadata.create_all(engine)

    session = Session(engine)

    results = session.query(State, City).filter(
                            City.state_id == State.id).order_by(
                            City.id).all()
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
