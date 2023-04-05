from flask import Flask
import mysql.connector

config = {
    'user' : 'auser',
    'password' : 'pass',
    'host' : 'localhost',
    'port' : '3306',
    'database' : 'dbcounter',
}

db = mysql.connector.connect(**config)



app = Flask(__name__)

@app.route('/')
def hello():
	return '<p>Hello welcome in the app!</p>'
    
@app.route('/count')
def dbcount():
	return '<p>The current count in the database is like {}</p>'

if __name__== "__main__":
	app.run("localhost", port=5000)

