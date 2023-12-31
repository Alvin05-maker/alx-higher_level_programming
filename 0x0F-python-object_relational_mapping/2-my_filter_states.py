#!/usr/bin/python3
""" List all the states from hbtn_0e_0_usa. """


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4]))

    result = cur.fetchall()
    for rows in result:
        print(rows)

    cur.close()
    db.close()
