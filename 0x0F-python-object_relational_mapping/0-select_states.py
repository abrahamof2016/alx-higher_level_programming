#!/usr/bin/python3
""""
lists all script from a database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            port=3306,
            db=argv[3])
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY id ASC;")
    for row in mycursor.fetchall():
        print(row)
    mycursor.close()
    db.close()
