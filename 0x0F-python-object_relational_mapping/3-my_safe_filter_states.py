#!/usr/bin/python3
""""
Takes an argument and Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
    sql = "SELECT * FROM states WHERE name = %s"
    parameters = [argv[4]]
    mycursor.execute(sql, parameters)
    for row in mycursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    mycursor.close()
    db.close()
