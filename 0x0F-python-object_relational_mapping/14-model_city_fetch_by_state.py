#!/usr/bin/python3
""" This module has the script to:
    Display all the cities and their states"""


if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    USER = argv[1]
    PASS = argv[2]
    DBNAME = argv[3]
    URL = f"mysql://{USER}:{PASS}@localhost/{DBNAME}"

    engine = create_engine(URL, pool_pre_ping=True)
    sessionmaker = sessionmaker(bind=engine)
    session = sessionmaker()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
