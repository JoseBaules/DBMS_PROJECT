from flask import Flask 
from views import views
from flask_mysqldb import MySQL
from database import mysql
 
app = Flask(__name__)   
app.register_blueprint(views,url_prefix="/views")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'jabaules'
app.config['MYSQL_PASSWORD'] = 'kees8On1'
app.config['MYSQL_DB'] = 'jabaules'

mysql.init_app(app)

if __name__ == '__main__':

    app.run(debug=True, port= 80000)
