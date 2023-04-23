import sys
import traceback
import logging
import database 


mysql_username = 'jmm101'  # please change to your username
mysql_password = 'saeth3Ie'  # please change to your MySQL password

try:
    database.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
    
    res = database.executeSelect('SELECT * FROM JOBS;')

    res = res.split('\n')  # split the header and data for printing

    print("<br/>" + "Table JOBS before:"+"<br/>" + res[0] + "<br/>"+res[1] + "<br/>")

    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    # insert into item tables by getting the values passed from PHP
    JobId = sys.argv[1]
    Cname = sys.argv[2]
    JobTitle = sys.argv[3]
    Salary = sys.argv[4]
    DesiredMajor = sys.argv[5]

    # next_id = database.nextId("JOBS")

    values = "'" + JobId + "', '" + Cname + "', '" + JobTitle + "', '" + Salary + "', '" +  DesiredMajor + "'"


    database.insert("JOBS", values)
    res = database.executeSelect('SELECT * FROM JOBS;')
    res = res.split('\n')  # split the header and data for printing
    
    # print("<br/>" + "<br/>")
    # print("<br/>" + "Table JOBS after:"+
    #       "<br/>" +
    #       res[0] + "<br/>"+res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    database.close_db()  # close db
except Exception as e:
    logging.error(traceback.format_exc())
