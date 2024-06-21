#!/usr/bin/python3

""" Displaying states that matches given name """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    USERNAME = argv[1]
    PASS = argv[2]
    DBNAME = argv[3]
    data = argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=USERNAME,
        passwd=PASS,
        db=DBNAME,
        charset="utf8"
    )
    cursor = conn.cursor()
    QUERY = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
    cursor.execute(QUERY.format(data))
    states = cursor.fetchall()
    for state in states:
        print(state)
