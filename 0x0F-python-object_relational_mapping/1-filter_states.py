#!/usr/bin/python3
"""
a script that lists all states tarting with an N from database
"""

import MySQLdb
from sys import argv, stderr


def listOf_States_Starting_With_N():
    """function to list only the states that start with N in given database"""

    err_message = "usage: {} <username> <password> <db_name>\n".format(argv[0])
    if len(argv) != 4:
        stderr.write(err_message)
        return

    username, password, db_name = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host="localhost",
	user=username,
	passwd=password,
	db=db_name,
	charset="utf8",
	port=3306
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    results = cur.fetchall()

    for line in results:
        print(line)

    db.close()


if __name__ == "__main__":
    listOf_States_Starting_With_N()
