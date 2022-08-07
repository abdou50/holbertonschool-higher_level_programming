#!/usr/bin/python3
"""script that lists all states from the database"""
import MySQLdb
from sys import argv


if name == "main":
    """make a connectin"""
    db_connection = MySQLdb.connect(host='localhost',
                                    port=3306,
                                    user=argv[1],
                                    password=argv[2],
                                    database=argv[3])

    """create a cursor"""
    c = db_connection.cursor()

    """execute query"""
    c.execute("SELECT * FROM states ORDER BY id ASC")
    i = c.fetchall()
    for j in i:
        print(j)

    """close all cursor and database"""
    c.close()
    db_connection.close()
