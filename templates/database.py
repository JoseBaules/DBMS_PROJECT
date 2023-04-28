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
   
    return(tabulate(result, headers=header))  # print results in table format

def executeSelect(query):
    cursor.execute(query)
    res = cursor.fetchall()
    return res


def insert(table, values):

    query = "SELECT COUNT(*) FROM " + table + ";"
    cursor.execute(query)
    result1 = cursor.fetchone()
    
    if table == "APPLICATIONS": 
        
        query = "SELECT StudentId FROM STUDENTS WHERE StudentId ="+values[1]+";"
        cursor.execute(query)
        result1 = cursor.fetchone()
        
    
        if int(values[1]) == int(result1[0]):
            query = "INSERT into " + table + " values (" + values[0] + ")" + ';'
            cursor.execute(query)
            conn.commit()
            result1 = cursor.fetchone()
            
            return True 
        else:

            return False
    else:
        
        query = "INSERT into " + table + " values (" + values[0] + ")" + ';'
        cursor.execute(query)
        conn.commit()
        #result1 = cursor.fetchone()

        query = "SELECT COUNT(*) FROM " + table + ";"
        cursor.execute(query)
        result2 = cursor.fetchone()

        if result2>result1:
            return True
        else:
            return False
    

def nextId(table):
    query = "select IFNULL(max(StudentId), 0) as max_id from " + table
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    return 1 if result is None else int(result) + 1





def close_db():  # use this function to close db
    cursor.close()
    conn.close()