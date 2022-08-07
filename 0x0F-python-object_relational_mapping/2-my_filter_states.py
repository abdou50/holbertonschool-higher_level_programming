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
    cur.execute("select * from states where name LIKE '{:s}' ORDRE BY id"
                .format(argv[4]))
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
