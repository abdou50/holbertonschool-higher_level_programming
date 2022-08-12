#!/usr/bin/python3
"""sql"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[
        1], passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities, states \
            WHERE cities.state_id = states.id ORDER BY cities.id ASC")
    i = cur.fetchall()
    for row in i:
        print(row)
    cur.close()
    conn.close()
