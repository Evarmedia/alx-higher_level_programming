import MySQLdb
import sys

def list_states_starting_with_n(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect("localhost", user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve states starting with 'N' and sort by id
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
    cursor.execute(query)

    # Fetch all the rows
    data = cursor.fetchall()

    # Display results
    for state in data:
        print(state)

    # Close the connection
    db.close()

if __name__ == "__main__":
    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function with provided arguments
    list_states_starting_with_n(username, password, database)

