#!/usr/bin/python3
"""
takes argument and list all states matching user input in database `hbtn_0e_0_usa`
this version is safe from MySQL injection
"""

import MySQLdb
from sys import argv, stderr


def get_States():
    """list all states matching user input in database `hbtn_0e_0_usa`"""

    err_mssg = "usage: {} <username> <passwd> <db_name> <state_name>\n".format(
        argv[0])

    if len(argv) != 5:
        stderr.write(err_mssg)
        return

    username, password, db_name, state = argv[1], argv[2], argv[3], argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8",
        port=3306
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(query, (state,))
    result = cur.fetchall()

    for state in result:
        print(state)

    db.close()


if __name__ == "__main__":
    get_States()
