#!/usr/bin/python3
"""
Script--> return states starting with 'N'
params: username, password & database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Data base connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # enable cursor && filter names (starting with 'N')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for r in cursor.fetchall():
        if r[1][0] == 'N':
            print(r)
    cursor.close()
    db.close()
