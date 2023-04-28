#!/usr/bin/env python

import subprocess
import cgi



def run():
    form = cgi.FieldStorage()

    JobId = form.getfirst('JobId', '')
    CompanyName = form.getfirst('CompanyName', '')
    JobTitle = form.getfirst('JobTitle', '')
    Salary = form.getfirst('Salary', '')
    DesiredMajor = form.getfirst('Smajor', '')


    result = subprocess.call(['python3', 'addJob.py', JobId, CompanyName, JobTitle, Salary, DesiredMajor])
    return result
    
if __name__ == '__main__':
    try:
        # Tell the browser it's an HTML page.
        print('Content-Type: text/html')
        # Blank line to indicate end of headers.
        print('')
        # Main program.
        if run():   
            print("""
                <!DOCTYPE html>
                <html>
                    <head>
                        <style>
                            p {
                                text-align: center;
                                margin-top: 20px;
                                font-size: 20px;
                                font-weight: bold;
                                color: #007bff;
                            }
                            button {
                                margin: 0 auto;
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
                            body {
                                display: flex;
                                justify-content: center;
                                align-items: center;
                                flex-direction: column;
                                height: 100vh;
                                background-image: url('background.png');
                                }

                                h1, button {
                                margin: 1em;
                                }
                        </style>
                    </head>
                    <body>
                        <a href="index.html" style="position: absolute; top: 0; left: 0;"><img src="home.png" style="width: 50px; height: 50px;"></a>

                        <h1>Job Added Successfully</h1>
                        <form action="http://csce.uark.edu/~jabaules/FinalProject/templates/inputJob.html" method="POST">
                            <button onclick="window.location.href='http://csce.uark.edu/~jabaules/FinalProject/templates/inputJob.html'">Add More Jobs</button>
                        </form>
                    </body>
                </html>
            """)
        else:
            print("""
                <!DOCTYPE html>
                <html>
                    <head>
                        <style>
                            p {
                                text-align: center;
                                margin-top: 20px;
                                font-size: 20px;
                                font-weight: bold;
                                color: #007bff;
                            }
                            button {
                                margin: 0 auto;
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
                            body {
                                display: flex;
                                justify-content: center;
                                align-items: center;
                                flex-direction: column;
                                height: 100vh;
                                background-image: url('background.png');
                                }

                                h1, button {
                                margin: 1em;
                                }
                        </style>
                    </head>
                    <body>
                        <a href="index.html" style="position: absolute; top: 0; left: 0;"><img src="home.png" style="width: 50px; height: 50px;"></a>

                        <h1>Impossible To Add Job</h1>
                        <form action="http://csce.uark.edu/~jabaules/FinalProject/templates/inputJob.html" method="POST">
                            <button onclick="window.location.href='http://csce.uark.edu/~jabaules/FinalProject/templates/inputJob.html'">Try Again</button>
                        </form>
                    </body>
                </html>
            """)


    except:
        cgi.print_exception()
