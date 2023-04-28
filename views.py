from flask import Blueprint,render_template, jsonify
from database import mysql

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    
    return render_template("index.html")

@views.route('/test')
def test():
    try:
        connection = mysql.connection
        cursor = connection.cursor()
        cursor.execute('SELECT VERSION()')
        version = cursor.fetchone()[0]
        return jsonify(success=True, message=f'Successful connection to MySQL server. Server version: {version}')
    except Exception as e:
        return jsonify(success=False, message=f'Error connecting to MySQL server: {e}')

@views.route('/jobs')
def jobs():
    
    return render_template("jobs.html")


@views.route('/add_student')
def add_student():

    print("running add_student web page....")
    return render_template('add_student.html')
