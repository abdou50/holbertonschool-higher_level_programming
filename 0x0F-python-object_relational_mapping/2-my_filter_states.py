#!/usr/bin/python3
"""sql"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC"
                .format(argv[4]))
    i = cur.fetchall()
    for row in i:
        print(row)
    cur.close()
    conn.close()
