from flask import Flask, redirect, url_for, request
from flask_mysqldb import MySQL
from datetime import date
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'deproject'
mysql = MySQL(app)


@app.route('/success/<name>')
def success(name):

#Executing SQL Statements

   with app.app_context():
      amt=100.0
      q="INSERT INTO fine (tagid, fineamt, entry_date) VALUES ('{}', {}, {})".format(name, amt, 'CURDATE()')
      cursor = mysql.connection.cursor()
      cursor.execute(q)
      mysql.connection.commit()
    # Applying changes
      cursor.execute("SELECT * FROM fine")

      data = cursor.fetchall()
      
      print(data)
   return 'welcome %s' % name





if __name__ == '__main__':
   app.run(debug = True,host='0.0.0.0')