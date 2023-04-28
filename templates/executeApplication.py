import sys
import traceback
import logging
import database as database 


mysql_username = 'jmm101'  # please change to your username
mysql_password = 'saeth3Ie'  # please change to your MySQL password
studentid = sys.argv[1]
jobId = sys.argv[2]

try:
    database.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
    
    values = "'" + studentid + "', '" +jobId + "'"
    
    res = database.insert("APPLICATIONS", [values,studentid])
    
    database.close_db()  # close db

    if res==True:
        sys.exit(True)
    else:
        sys.exit(False)



except Exception as e:
    logging.error(traceback.format_exc())
