#!/usr/bin/python3
""""
 lists all cities within given states from the database hbtn_0e_4_usa
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
    try:
        mycursor.execute(
        "SELECT cities.name FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])
    except MySQLdb.Error as e:
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print ("MySQL Error: %s" % str(e))
    row_list = mycursor.fetchall()
    printed_row = 0
    for row in row_list:
        if printed_row < len(row_list) - 1:
            print("{}, ".format(row[0]), end="")
            printed_row += 1
        else:
            print("{}".format(row[0]))
    mycursor.close()
    db.close()
