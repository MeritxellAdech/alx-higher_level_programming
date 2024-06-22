#!/usr/bin/python3
""" Deleting all object states whose names contains 'a' """


if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from sqlalchemy import create_engine, func
    from sqlalchemy.orm import sessionmaker

    USER = argv[1]
    PASS = argv[2]
    DBNAME = argv[3]
    URL = f"mysql://{USER}:{PASS}@localhost/{DBNAME}"

    engine = create_engine(URL, pool_pre_ping=True)
    sessionmaker = sessionmaker(bind=engine)
    session = sessionmaker()

    states = session.query(State).filter(func.binary(State.name).like('%a%'))\
        .all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
