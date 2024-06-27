#!/usr/bin/python3

""" This modules handles the relationship between state and city"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import State

    USER = argv[1]
    PASWD = argv[2]
    DBNAME = argv[3]
    URL = f"mysql://{USER}:{PASWD}@localhost/{DBNAME}"

    # Creating the engine
    engine = create_engine(URL, pool_pre_ping=True)
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Preparing the records
    state = State(name="California")
    city = City(name="San Francisco", state_id=state.id)
    state.cities.append(city)

    # inserting records in the table
    session.add(state)
    session.add(city)

    # Persisting the changes
    session.commit()
