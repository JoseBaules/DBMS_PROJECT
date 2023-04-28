import sys
import traceback
import logging
import database as database 


mysql_username = 'jmm101'  # please change to your username
mysql_password = 'saeth3Ie'  # please change to your MySQL password

try:
    database.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
    
    res = database.executeSelect('SELECT * FROM JOBS;')

    JobId = sys.argv[1]
    Cname = sys.argv[2]
    JobTitle = sys.argv[3]
    Salary = sys.argv[4]
    DesiredMajor = sys.argv[5]

    # next_id = database.nextId("JOBS")

    values = "'" + JobId + "', '" + Cname + "', '" + JobTitle + "', '" + Salary + "', '" +  DesiredMajor + "'"


    res = database.insert("JOBS", [values,JobId])
    
    database.close_db()  # close db

    if res==True:
        sys.exit(True)
    else:
        sys.exit(False)
        
except Exception as e:
    logging.error(traceback.format_exc())
