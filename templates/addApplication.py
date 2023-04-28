import sys
import traceback
import logging
import database as database 


mysql_username = 'jmm101'  # please change to your username
mysql_password = 'saeth3Ie'  # please change to your MySQL password

try:
    database.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
    res = database.executeSelect("SELECT JobId, JobTitle FROM JOBS")
    

    html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Add an Application</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    font-size: 16px;
                    margin: 50px auto;
                    width: 50%;
                    background-image: url('background.png');
                }
                
                form {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    margin-top: 20px;
                }
                
                label {
                    margin-top: 20px;
                }
                
                select, input {
                    padding: 8px;
                    border-radius: 4px;
                    border: 1px solid #ccc;
                    width: 100%;
                    font-size: 16px;
                }
                
                button {
                    margin-top: 20px;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 4px;
                    background-color: #007bff;
                    color: #fff;
                    font-size: 16px;
                    cursor: pointer;
                    transition: background-color 0.3s ease;
                }
                
                button:hover {
                    background-color: #0062cc;
                }
            </style>
        </head>
        <body>
            <a href="index.html" style="position: absolute; top: 0; left: 0;"><img src="home.png" style="width: 50px; height: 50px;"></a>

            <h3>Add Application:</h3>
            <form action="executeApplication.cgi" method="POST">
                <label for="StudentId">Enter Student ID:</label>
                <input type="text" id="StudentId" name="StudentId">
                
                <label for="JobId">Select a Job:</label>
                <select id="JobId" name="JobId">
    """

    res = database.executeSelect("SELECT JobId, JobTitle, CompanyName FROM JOBS")

    for row in res:
        option_text = "Title: {} | ID: {} | Company: {}".format(row[1], row[0],row[2])
        html_content += "<option value='{}'>{}</option>".format(row[0], option_text)

    
    html_content += """
                </select>
                
                <button type="submit">Submit</button>
            </form>
        </body>
        </html>
    """
   
    print("Content-Type: text/html")
    print()
    print(html_content)
    
    database.close_db()  # close db
except Exception as e:
    logging.error(traceback.format_exc())
