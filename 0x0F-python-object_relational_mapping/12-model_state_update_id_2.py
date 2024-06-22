#!/usr/bin/python3
""" Updating a state """


if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    USER = argv[1]
    PASS = argv[2]
    DBNAME = argv[3]
    URL = f"mysql://{USER}:{PASS}@localhost/{DBNAME}"

    engine = create_engine(URL, pool_pre_ping=True)
    sessionmaker = sessionmaker(bind=engine)
    session = sessionmaker()

    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
