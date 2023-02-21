#!/usr/bin/python3
"""
Script--> return matching states
params: username, password, database, state to be matched
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

    # enable cursor && match arg given
    cursor = db.cursor()
    sql_cmd = """SELECT *
                 FROM states
                 WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
    cursor.execute(sql_cmd)
    for r in cursor.fetchall():
        if r[1] == argv[4]:
            print(r)
    cursor.close()
    db.close()
