#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb as db

if __name__ == "__main__":

    list = sys.argv
    username, password, database = (list[1], list[2], list[3])
    connection = db.connect(host = "localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
