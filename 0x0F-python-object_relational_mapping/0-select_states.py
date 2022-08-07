#!/usr/bin/python3
"""sql"""
if __name__ == "__main__":
    import MySQLdb
    import sys as n
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=n.argv[1],
        passwd=n.argv[2],
        db=n.argv[3],
        charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY state.id ASC")
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
