#!/usr/bin/python3
""" Display the first row from the State table"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import State

    USERNAME = argv[1]
    PASS = argv[2]
    DBNAME = argv[3]
    URL = "mysql://{}:{}@localhost/{}"

    # Create engine object
    engine = create_engine(
        URL.format(USERNAME, PASS, DBNAME),
        pool_pre_ping=True)
    # Create a session
    sessionmaker = sessionmaker(bind=engine)
    # activating the session
    session = sessionmaker()
    # querying to get the first state
    name = session.query(State).order_by(State.id).first()
    if name is not None:
        print(f"{name.id}: {name.name}")
    else:
        print("Nothing")
