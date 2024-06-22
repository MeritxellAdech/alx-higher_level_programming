#!/usr/bin/python3
""" Retrieves the id of the given state """


if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    USER = argv[1]
    PASS = argv[2]
    DBNAME = argv[3]
    STATE = argv[4]
    URL = f"mysql://{USER}:{PASS}@localhost/{DBNAME}"

    engine = create_engine(URL, pool_pre_ping=True)
    sessionmaker = sessionmaker(bind=engine)
    session = sessionmaker()

    state_obj = session.query(State).filter(State.name == STATE).first()
    if state_obj is None:
        print("Not found")
    else:
        print(state_obj.id)
