#!/usr/bin/python3

""" 
a script that lists all states from database
"""
import MySQLdb
from sys import argv, stderr

def listStates():
    """function to list the states in a given database"""
    err_message = "usage: {} <username> <password> <db_name>\n".format(argv[0])
    if len(argv) != 4:
        stderr.write(err_message)
        return
    username, password, db_name = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(
        host = "localhost",
	user = username,
	passwd = password,
	db = db_name,
	charset = "utf8",
	port = 3306
    )

    cur = db.cursor()
    cur.exexute("SELECT * FROM states ORDER BY id ASC")
    result = cur.fetchall()
    
    for row in results:
        print(row)

    db.close()
if __name__ == "__main__":
    listStates()
