#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    queries = "SELECT cities.name FROM cities"
    queries = queries + " INNER JOIN states ON cities.state_id = states.id"
    queries = queries + " WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(queries, [sys.argv[4]])
    stat = cur.fetchall()
    print(", ".join([row[0] for row in stat]))
    cur.close()
    conn.close()
