#!/usr/bin/python3
"""sql"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    connected = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    string = connected.cursor()
    string.execute("SELECT *  states ORDRE BY states.id ASC")
    rowfetch = cursor.fetchall()
    for row in rowfetch:
       print(row)
    string.close()
    connected.close()
