import sys
import traceback
import logging
import database as database

mysql_username = 'jmm101'  # please change to your username
mysql_password = 'saeth3Ie'  # please change to your MySQL password

try:
    database.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database

    major = sys.argv[1]


    if major == 'ALL':
        res = database.executeSelect("SELECT * FROM STUDENTS;")
    else: 
        res = database.executeSelect("SELECT * FROM STUDENTS WHERE Major= '" + major + "';")
        



    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Students List - Python CGI Script Example</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                font-size: 16px;
                margin: 0;
                padding: 0;
                background-image: url('background.png');

            }}
            
            h1 {{
                text-align: center;
                margin-top: 50px;
            }}
            
            p {{
                text-align: center;
                margin-bottom: 50px;
            }}
            
            table {{
                margin: 0 auto;
                border-collapse: collapse;
                width: 80%;
            }}
            
            th, td {{
                padding: 12px;
                text-align: center;
                border-bottom: 1px solid #ddd;
            }}
            
            th {{
                background-color: #007bff;
                color: #fff;
            }}
            
                    /* Search bar style */
                    .search {{
                        margin-bottom: 20px;
                    }}

                    .search label {{
                        font-weight: bold;
                        display: block;
                        margin-bottom: 5px;
                    }}

                    .search input[type="text"] {{
                        padding: 10px;
                        font-size: 16px;
                        border-radius: 5px;
                        border: none;
                        width: 100%;
                        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
                    }}

                    .search input[type="text"]:focus {{
                        outline: none;
                        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.5);
                    }}
            
        </style>
    </head>
    <body>
        
        <a href="index.html"><img src="home.png" style="width: 50px; height: 50px;"></a>
        <h1>Students List</h1>
        
        <div class="search">
                    <label for="JobId">Enter a value:</label>
                    <input type="text" placeholder="Search.." id="searchInput">
        </div>

        <table>
            <thead>
                <tr>
                    <th>Student ID</th>
                    <th>Student Name</th>
                    <th>Major</th>
                </tr>
            </thead>
            <tbody>
    """

    for row in res:
        html_content += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"

    html_content += """
            </tbody>
        </table>
        <script>
                    
            var searchInput = document.getElementById("searchInput");
            searchInput.addEventListener("input", function() {
                var filter = this.value.toLowerCase();
                var rows = document.getElementsByTagName("tr");
                for (var i = 0; i < rows.length; i++) {
                    var row = rows[i];
                    if (row.getElementsByTagName("th").length == 0) {
                        var cells = row.getElementsByTagName("td");
                        var shouldShow = false;
                        for (var j = 0; j < cells.length; j++) {
                            var cell = cells[j];
                            if (cell.textContent.toLowerCase().indexOf(filter) > -1) {
                                shouldShow = true;
                                break;
                            }
                        }
                        if (shouldShow) {
                            row.style.display = "";
                        } else {
                            var nameCell = row.getElementsByTagName("td")[0];
                            if (nameCell.textContent.toLowerCase().indexOf(filter) > -1) {
                                row.style.display = "";
                            } else {
                                row.style.display = "none";
                            }
                        }
                    }
                }
            });
        </script>
    </body>
    </html>
    """



    print(html_content)

except Exception as e:
    logging.error(traceback.format_exc())
