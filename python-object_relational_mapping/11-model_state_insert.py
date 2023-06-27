#!/usr/bin/python3
"""
Module lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    # Define the database uri
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    # Create engine and session
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a state object and add it to the session
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # print the results
    print(new_state.id)
