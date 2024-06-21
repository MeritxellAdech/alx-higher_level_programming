#!/usr/bin/python3

"""This module displays all states that begin with N """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    USERNAME = argv[1]
    PASS = argv[2]
    DBNAME = argv[3]
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=USERNAME,
        passwd=PASS,
        db=DBNAME,
        charset="utf8"
        )
    QUERY = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cur = con.cursor()
    cur.execute(QUERY)
    n_states = cur.fetchall()
    for state in n_states:
        print(state)
    cur.close()
    con.close()
