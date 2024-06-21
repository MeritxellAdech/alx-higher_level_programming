#!/usr/bin/python3

"""Displays all the cities of the given state"""


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

    QUERY = "SELECT c.name \
        FROM cities c INNER JOIN states s \
        ON s.id = state_id \
        WHERE s.name = %s \
        ORDER BY c.id ASC"
    cursor = conn.cursor()
    cursor.execute(QUERY, {data})
    resultset = cursor.fetchall()
    length = len(resultset)
    i = 1
    all = []

    for row in resultset:
        all.append(', '.join(map(str, row)))
    s = ', '.join(all)
    print(s)
    cursor.close()
    conn.close()
