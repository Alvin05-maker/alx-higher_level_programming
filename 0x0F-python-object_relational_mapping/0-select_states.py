#!/usr/bin/python3
"""List all states from the states table in the hbtn_0e_0_usa database"""


import sys
import MySQLdb

if __name__== "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor() # Creating cursor object for interacting with the database
    cur.execute("SELECT * FROM states") #Query all states from the states table
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()

