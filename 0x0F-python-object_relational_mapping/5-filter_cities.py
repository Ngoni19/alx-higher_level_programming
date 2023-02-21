#!/usr/bin/python3
"""
Script--> return cities in the state given (tables 'cities' 'states)
params: username, password, database & state
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
    SQL_cmd = """SELECT cities.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name LIKE %s
                 ORDER BY cities.id ASC"""
    cursor.execute(SQL_cmd, (argv[4], ))

    # print cities of same state (;)
    print(', '.join(["{:s}".format(r[0]) for r in cursor.fetchall()]))

    cursor.close()
    db.close()
