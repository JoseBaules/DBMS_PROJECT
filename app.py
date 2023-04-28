#!/usr/bin/env python

import os
import sys
from flask import Flask, render_template, request
import subprocess
from views import views
from database import mysql
import cgi

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':

        Id = request.form['StudentId']
        # get the name input value
        name = request.form['Sname']
        # sanitize the input to prevent shell injection attacks
        # name = subprocess.list2cmdline([name])

        # Id = subprocess.list2cmdline([Id])

        major = request.form['Smajor']
        # major = subprocess.list2cmdline([major])


        # build the command to run the Python script
        command = f'python3 addStudent.py {Id} "{name}" "{major}"'


        # run the command and capture the output
        output = subprocess.check_output(command, shell=True)

        # return the output to the web page
        return render_template('index.html', output=output.decode('utf-8'))
    else:
        # display the input form
        return render_template('input.html')

@app.route('/add-job', methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':

        # get the name input value
        JobId = request.form['JobId']
        # sanitize the input to prevent shell injection attacks
        # name = subprocess.list2cmdline([name])
        CompanyName = request.form['CompanyName']

        # Id = subprocess.list2cmdline([Id])

        JobTitle = request.form['JobTitle']
        # major = subprocess.list2cmdline([major])

        Salary = request.form['Salary']

        DesiredMajor = request.form['DesiredMajor']
        

        # build the command to run the Python script
        command = f'python3 addJob.py {JobId} "{CompanyName}" "{JobTitle}" {Salary} "{DesiredMajor}"'


        # run the command and capture the output
        output = subprocess.check_output(command, shell=True)

        # return the output to the web page
        return render_template('index.html', output=output.decode('utf-8'))
    else:
        # display the input form
        return render_template('inputJob.html')
    

@app.route('/add-application', methods=['GET', 'POST'])
def add_application():
    if request.method == 'POST':

        StudentId = request.form['StudentId']
        # get the name input value
        JobId = request.form['JobId']
        # sanitize the input to prevent shell injection attacks
        # name = subprocess.list2cmdline([name])

        # build the command to run the Python script
        command = f'python3 addApplication.py {StudentId} "{JobId}"'


        # run the command and capture the output
        output = subprocess.check_output(command, shell=True)

        # return the output to the web page
        return render_template('index.html', output=output.decode('utf-8'))
    else:
        # display the input form
        return render_template('inputApplications.html')

@app.route('/view-students', methods=['GET', 'POST'])
def view_all_students():
        
    # build the command to run the Python script
    command = f'python3 viewStudents.py'


    # run the command and capture the output
    # output = subprocess.check_output(command)
    output = subprocess.check_output(command, shell=True)


    # return the output to the web page
    return render_template('viewStudents.html', output=output.decode('utf-8'))

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

# mysql.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=8002)
