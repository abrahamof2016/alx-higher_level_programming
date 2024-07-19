#!/usr/bin/python3
""""
 lists all cities from the database hbtn_0e_4_usa
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
    mycursor.execute(
            "SELECT cities.name FROM cities\
                    INNER JOIN states\
                    ON cities.state_id = states.id\
                    WHERE states.name = %s", [argv[4]])
    for row in mycursor.fetchall():
        print(row[0], end=", ")
    print()
    mycursor.close()
    db.close()
