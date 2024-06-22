#!/usr/bin/python3
""" Displaying all states the contains 'a' """

if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from sqlalchemy import create_engine, func
    from sqlalchemy.orm import sessionmaker

    USERNAME = argv[1]
    PASS = argv[2]
    DBNAME = argv[3]
    URL = f"mysql://{USERNAME}:{PASS}@localhost/{DBNAME}"

    engine = create_engine(URL, pool_pre_ping=True)
    sessionmaker = sessionmaker(bind=engine)
    session = sessionmaker()

    objs = session.query(State).filter(func.binary(State.name).like('%a%')).\
        order_by(State.id).all()
    for state in objs:
        print(f"{state.id}: {state.name}")
