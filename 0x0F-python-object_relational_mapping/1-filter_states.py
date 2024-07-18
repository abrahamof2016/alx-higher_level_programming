#!/usr/bin/python3
""""
lists all states with a name starting with N (upper N) from database.
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306)
    mycursor = db.cursor()
    mycursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    for row in mycursor.fetchall():
        if row[1][0] == 'N':
            print(row)
    mycursor.close()
    db.close()
