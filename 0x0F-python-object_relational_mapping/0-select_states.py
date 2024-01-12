#!/usr/bin/python3

"""
 lists all states from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    user_name=sys.argv[1]
    password=sys.argv[2]
    db_name=sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user, passwd=password, db=db_name)
    cursor = b.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
