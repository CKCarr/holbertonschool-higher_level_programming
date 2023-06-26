#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

def filter_states(mysql_username, mysql_password, database_name, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Prepare the SQL query with user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Display the results
    for state in results:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_states(mysql_username, mysql_password, database_name, state_name)
