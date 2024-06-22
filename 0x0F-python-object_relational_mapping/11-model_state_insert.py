#!/usr/bin/python3
""" Inserting an object in the database """


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

    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()

    state = session.query(State).filter(State.name == "Louisiana").first()
    print(state.id)
