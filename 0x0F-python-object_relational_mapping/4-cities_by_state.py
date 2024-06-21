#!/usr/bin/python3

""" Displaying all available cities """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    USERNAME = argv[1]
    PASS = argv[2]
    DBNAME = argv[3]

    data = "SELECT c.id, c.name, s.name \
        FROM cities c INNER JOIN states s \
        ON s.id = state_id \
        ORDER BY c.id ASC"
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=USERNAME,
        passwd=PASS,
        db=DBNAME,
        charset="utf8"
    )
    cursor = conn.cursor()
    cursor.execute(data)
    resultset = cursor.fetchall()
    for row in resultset:
        print(row)
    cursor.close()
    conn.close()
