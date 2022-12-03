#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":

    list_arg = sys.argv
    username, password, database = (list_arg[1], list_arg[2], list_arg[3])
    connection = MySQLdb.connect(host = "localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
