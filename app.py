from flask import Flask
# import mysql.connector

# config = {
#     'user' : 'root',
#     'password' : 'pass',
#     'host' : '127.0.0.1',
#     'database' : 'dbcounter',
# }

# db = mysql.connector.connect(**config)

app = Flask(__name__)

@app.route('/')
def hello():
	return '<p>Hello welcome in the app!</p>'
    
# @app.route('/count')
# def dbcount():
# 	return '<p>The current count in the database is like {}</p>'

if __name__== "__main__":
	app.run(host="127.0.0.1", port=5000)

