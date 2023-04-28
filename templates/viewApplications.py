import os
import sys
import traceback
import logging
import database as database

mysql_username = 'jmm101'
mysql_password = 'saeth3Ie'

try:
    database.open_database('localhost', mysql_username, mysql_password, mysql_username)
    
    
    # res = database.executeSelect("SELECT studentId, jobID FROM APPLICATIONS")

    # Get selected major from Smajor dropdown list
    selected_major = os.environ.get('Smajor', 'all')

    # Modify SQL query based on selected major
    if selected_major == 'all':
        query = "SELECT STUDENTS.StudentName, JOBS.JobTitle, JOBS.CompanyName, JOBS.Salary, STUDENTS.Major FROM APPLICATIONS \
                            INNER JOIN STUDENTS ON APPLICATIONS.StudentId = STUDENTS.StudentId \
                            INNER JOIN JOBS ON APPLICATIONS.JobID = JOBS.JobId;"
    else:
        query = "SELECT STUDENTS.StudentName, JOBS.JobTitle, JOBS.CompanyName, JOBS.Salary, STUDENTS.Major FROM APPLICATIONS \
                            INNER JOIN STUDENTS ON APPLICATIONS.StudentId = STUDENTS.StudentId \
                            INNER JOIN JOBS ON APPLICATIONS.JobID = JOBS.JobId \
                            WHERE STUDENTS.Major = '{}';".format(selected_major)


    res = database.executeSelect(query)



    html_content = """
        <!DOCTYPE html>
    <html>
    <head>
        <title>Python CGI Script Example</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                font-size: 16px;
                background-image: url('background.png');

            }
            
            h1 {
                text-align: center;
                margin-top: 50px;
            }
            
            table {
                margin: 50px auto;
                border-collapse: collapse;
                width: 80%;
            }
            
            th, td {
                padding: 12px;
                text-align: center;
                border-bottom: 1px solid #ddd;
            }
            
            th {
                background-color: #007bff;
                color: #fff;
            }
            
    /* Search bar style */
    .search {
        margin-bottom: 20px;
    }

    .search label {
        font-weight: bold;
        display: block;
        margin-bottom: 5px;
    }

    .search input[type="text"] {
        padding: 10px;
        font-size: 16px;
        border-radius: 5px;
        border: none;
        width: 100%;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    }

    .search input[type="text"]:focus {
        outline: none;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.5);
    }

    /* Filter buttons style */
    #myBtnContainer {
        margin-bottom: 20px;
    }

    .btn {
        border: none;
        background-color: #f1f1f1;
        color: black;
        padding: 12px 16px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 5px;
        margin-right: 10px;
        margin-bottom: 10px;
        transition: all 0.3s ease;
    }

    .btn:hover {
        background-color: #ddd;
    }

    .btn.active {
        background-color: #4CAF50;
        color: white;
    }
     th, td {
        text-align: left;
        padding: 8px;
        border-bottom: 1px solid #ddd;
    }
    .searchMajor label {
        font-weight: bold;
        display: block;
        margin-bottom: 5px;
    }
    select{
        padding: 8px 20px;
        font-size: 16px;
        border-radius: 4px;
        border: 1px solid #ccc;
        width: 200px;
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        background-color: #f1f1f1;
        background-image: url('arrow-down.png');
        background-position: right center;
        background-repeat: no-repeat;
    }

    select:hover {
    cursor: pointer;
    }

    select:focus {
    outline: none;
    box-shadow: 0 0 0 2px #aaa;
    border-color: #aaa;
    }
    </style>
    </head>
    <body>

    <a href="index.html"><img src="home.png" style="width: 50px; height: 50px;"></a>
        <h1>Applications</h1>
        

        <!-- Control buttons -->
        <div id="myBtnContainer">
        <button class="btn active" onclick="filterSelection('all')"> Show all</button>
        </div>
        <div class="searchMajor">
            <label for="JobId">Search by major:</label>
            <select name="Smajor" onchange="filterSelection(this.value)">
                <option value="all" {0}>All</option>
                <option value="Computer Science" {1}>Computer Science</option>
                <option value="Computer Engineering" {2}>Computer Engineering</option>
                <option value="Mechanical Engineering" {3}>Mechanical Engineering</option>
                <option value="Electrical Engineering" {4}>Electrical Engineering</option>
                <option value="Business" {5}>Business</option>
            </select>
        </div>


        <div class="search">
            <label for="JobId">Enter a value:</label>
            <input type="text" placeholder="Search.." id="searchInput">
        </div>




            <table>
            <thead class="table-header">
                <th>Student Name</th>
                <th>Major</th>
                <th>Company Name</th>
                <th>Salary</th>
                <th>Job Title</th>
            </thead>
            <tbody>
    """ 
    for row in res:
        html_content += "<tr class='filter-{}'><td>{}</td> <td>{}</td> <td>{}</td> <td>{}</td> <td>{}</td></tr>".format(row[4], row[0], row[4], row[2], row[3], row[1])

    html_content += """
        </tbody>
        </table>
<script>
    function filterSelection(filter) {
        var rows = document.getElementsByTagName("tr");
        for (var i = 0; i < rows.length; i++) {
            var row = rows[i];
            if (row.className.indexOf(filter) > -1 || filter === "all") {
                row.style.display = "";
            } else {
                // Check if the current row is not the header row before hiding it
                if (row.getElementsByTagName("th").length == 0) {
                    row.style.display = "none";
                }
            }
        }
    }
    var select = document.getElementsByName("Smajor")[0];
    select.addEventListener("change", function() {
        filterSelection(this.value);
    });


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

    print()
    print(html_content)

except Exception as e:
    logging.error(traceback.format_exc())
