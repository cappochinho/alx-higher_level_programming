#!/usr/bin/python3
"""
  Lists all the values in the states table of hbtn_0e_0_usa if name matches the argument
  Usage: ./1-filter_states.py <mysql username> \
                              <mysql password> \
                              <database name>  \
                              <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":

    list = sys.argv
    username, password, database = (list[1], list[2], list[3])
    connection = MySQLdb.connect(host = "localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `states` WHERE BINARY `name` = '{}'".format(list[4])) ORDER BY `id` ASC")
    [print(state) for state in cursor.fetchall()]
