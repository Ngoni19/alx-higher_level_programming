#!/usr/bin/python3
"""
Script--> return info from tables ('cities' 'states)
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

    # enable cursor && join two tables for all info
    cursor = db.cursor()
    SQL_cmd = """SELECT cities.id, cities.name, states.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 ORDER BY cities.id ASC"""
    cursor.execute(SQL_cmd)

    for r in cursor.fetchall():
        print(r)
    cursor.close()
    db.close()
