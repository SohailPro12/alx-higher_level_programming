#!/usr/bin/python3

"""
takes in the name of a state as an argument
and lists all cities of that state
using the database hbtn_0e_4_usa
"""


if __name__ == '__main__':

    import sys
    import MySQLdb

    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user_name, passwd=password, db=db_name)

    cursor = db.cursor()
    cursor.execute("SELECT cities.name\
                    FROM cities INNER JOIN states\
                    ON states.id=cities.state_id\
                    WHERE states.name=%s\
                    ORDER BY cities.id ASC; ", (state_name,))
    rows = cursor.fetchall()
    """for i, row in enumerate(rows):
        if i < len(rows) - 1:
            print(row[0], end=", ")
            i = i+1
        else:
            print(row[0], end="\n")"""
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
