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
    # check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python3 7-model_state_fetch_all.py \
              [mysql_username] [mysql_password] [database_name]")
        sys.exit(1)

    # get the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Define the database uri
    db_uri = f"mysql+mysqldb://{mysql_username}: \
    {mysql_password}@localhost:3306/{database_name}"

    # Create engine and session
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all state objects and sort by states.id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
