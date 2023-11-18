#!/usr/bin/python3
"""same as task 2, but write one that is safe from MySQL injections"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE Name =  %s ORDER BY id ASC",
                [sys.argv[4]])
    stat = cur.fetchall()
    for row in stat:
        print(row)
    cur.close()
    conn.close()
