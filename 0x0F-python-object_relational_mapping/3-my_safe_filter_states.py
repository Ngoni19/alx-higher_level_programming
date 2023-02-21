#!/usr/bin/python3
"""
Script--> return matching states.should be safe from MySQL injections
# http://bobby-tables.com/python
params: username, password, database && state to match
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
                 WHERE name=%s ORDER BY id ASC"""
    cursor.execute(sql_cmd, (argv[4],))

    for r in cursor.fetchall():
        print(r)
    cursor.close()
    db.close()
