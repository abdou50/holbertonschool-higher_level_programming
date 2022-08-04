#!/usr/bin/python3
"""sql"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    connected = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    string = connected.cursor()
    string = execute("select * from states ORDRE BY states.id")
    rowfetch = cursor.fetchall()
    for row in rowfetch:
       print(row)
    string.close()
    connected.close()
