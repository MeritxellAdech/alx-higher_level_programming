#!/usr/bin/python3
""" Retrieving all the names of the states found on the state table """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    USERNAME = argv[1]
    PASS = argv[2]
    DB_NAME = argv[3]
    # connect with the database
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=USERNAME,
        passwd=PASS,
        db=DB_NAME,
        charset="utf8",
    )
    # opening the cursor to interact with the database
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    selection = cur.fetchall()
    for row in selection:
        print(row)
    cur.close()
    con.close()
