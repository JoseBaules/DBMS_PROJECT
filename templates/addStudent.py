import sys
import traceback
import logging
import database as database 
from string import Template
import webbrowser

mysql_username = 'jmm101'  # please change to your username
mysql_password = 'saeth3Ie'  # please change to your MySQL password

try:
    database.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
    
    res = database.executeSelect('SELECT * FROM STUDENTS;')

    StudentId = sys.argv[1]
    Sname = sys.argv[2]
    Smajor = sys.argv[3]

    values = "'" + StudentId + "', '" + Sname + "', '" + Smajor + "' "
    res = database.insert("STUDENTS", [values,StudentId])
    database.executeSelect('SELECT * FROM STUDENTS;') 
        
    database.close_db()  # close db
    if res==True:
        sys.exit(True)
    else:
        sys.exit(False)


except Exception as e:
    logging.error(traceback.format_exc())


