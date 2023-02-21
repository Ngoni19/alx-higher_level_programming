#!/usr/bin/python3
"""
Script --> return all table ('states') values
param: username, password and database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Database connect
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # enable cursor for SQL
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for r in cursor.fetchall():
        print(r)
    cursor.close()
    db.close()
