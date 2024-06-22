#!/usr/bin/python3

""" Retrieving all states using ORM """
if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    USERNAME = argv[1]
    PASS = argv[2]
    DBNAME = argv[3]
    URL = "mysql://{}:{}@localhost/{}"

    engine = create_engine(
        URL.format(USERNAME, PASS, DBNAME),
        pool_pre_ping=True
        )
    sessionmaker = sessionmaker(bind=engine)
    session = sessionmaker()
    for row in session.query(State).order_by(State.id).all():
        print(f"{row.id}: {row.name}")
