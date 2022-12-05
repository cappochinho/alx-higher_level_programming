#!/usr/bin/python3
"""
Takes the name of a state as an argument and \
lists all the cities of that state
Usage: ./5-filter_cities.py <mysql username> \
                            <mysql password> \
                            <database name> \
                            <state name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    list = sys.argv
    username, password, database, state = (list[1], list[2], list[3], list[4])
    connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `cities` as `c` \
            INNER JOIN `states` as `s` \
            ON `c`.`state_id` = `s`.`id` ORDER BY `c`.`id`")
    print(", ".join([c[2] for c in cursor.fetchall() if c[4] == list[4]]))
