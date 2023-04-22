import sys
from flask import Flask, render_template, request
import subprocess
from views import views
from database import mysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':

        # get the name input value
        name = request.form['Sname']
        # sanitize the input to prevent shell injection attacks
        # name = subprocess.list2cmdline([name])

        Id = request.form['StudentId']

        major = request.form['Smajor']

        # build the command to run the Python script
        command = f'python3 addStudent.py {Id, name, major}'

        # run the command and capture the output
        output = subprocess.check_output(command, shell=True)

        # return the output to the web page
        return render_template('output.html', output=output.decode('utf-8'))
    else:
        # display the input form
        return render_template('input.html')

@app.route('/add-job')
def add_job():
    return render_template('input.html')

@app.route('/add-application')
def add_application():
    return render_template('input.html')

@app.route('/view-all-students')
def view_all_students():
    return render_template('students.html')

@app.route('/view-all-jobs')
def view_all_jobs():
    return render_template('jobs.html')

@app.route('/view-all-applications')
def view_all_applications():
    return render_template('applications.html')

app.register_blueprint(views,url_prefix="/views")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'jmm101'
app.config['MYSQL_PASSWORD'] = 'saeth3Ie'
app.config['MYSQL_DB'] = 'jmm101'

mysql.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
