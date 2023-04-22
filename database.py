# database.py
import mysql.connector
# from flask_mysqldb import MySQL
from tabulate import tabulate

# mysql = MySQL()

def open_database(hostname, user_name, mysql_pw, database_name):
    global conn
    conn = mysql.connector.connect(host=hostname,
                                   user=user_name,
                                   password=mysql_pw,
                                   database=database_name
                                   )
    global cursor
    cursor = conn.cursor()

def printFormat(result):
    header = []
    for cd in cursor.description:  # get headers
        header.append(cd[0])
    print('')
    print('Query Result:')
    print('')
    return(tabulate(result, headers=header))  # print results in table format

def executeSelect(query):
    cursor.execute(query)
    res = printFormat(cursor.fetchall())
    return res


def insert(table, values):
    query = "INSERT into " + table + " values (" + values + ")" + ';'
    cursor.execute(query)
    conn.commit()

def nextId(table):
    query = "select IFNULL(max(StudentId), 0) as max_id from " + table
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    return 1 if result is None else int(result) + 1





def close_db():  # use this function to close db
    cursor.close()
    conn.close()