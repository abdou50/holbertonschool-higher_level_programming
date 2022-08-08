#!/usr/bin/python3
"""sql"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connection = MySQLdb.connect(host='localhost',
                                    port=3306,
                                    user=argv[1],
                                    password=argv[2],
                                    database=argv[3]
                                    )
    c = db_connection.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    i = c.fetchall()
    for j in i:
        if j[1][0] == 'N':
            print(j)
    c.close()
    db_connection.close()
