import sys
import traceback
import logging
import database 


mysql_username = 'jmm101'  # please change to your username
mysql_password = 'saeth3Ie'  # please change to your MySQL password

try:
    database.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
    
    res = database.executeSelect('SELECT * FROM STUDENTS;')

    res = res.split('\n')  # split the header and data for printing

    print("<br/>" + "Table Students before:"+"<br/>" + res[0] + "<br/>"+res[1] + "<br/>")

    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    # insert into item tables by getting the values passed from PHP
    StudentId = sys.argv[1]
    StundetName = sys.argv[2]
    StundentMajor = sys.argv[3]

    # next_id = database.nextId("STUDENTS")

    values = "'" + StudentId + "','" + StundetName + "','" + StundentMajor + "'"


    database.insert("STUDENTS", values)
    res = database.executeSelect('SELECT * FROM STUDENTS;')
    res = res.split('\n')  # split the header and data for printing
    print("<br/>" + "<br/>")
    print("<br/>" + "Table Students after:"+"<br/>" +
          res[0] + "<br/>"+res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    database.close_db()  # close db
except Exception as e:
    logging.error(traceback.format_exc())
