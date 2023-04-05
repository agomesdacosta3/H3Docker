import mysql.connector

config = {
    'user' : 'auser',
    'password' : 'pass',
    'host' : 'localhost',
    'port' : '3306',
    'database' : 'dbcounter',
}

db = mysql.connector.connect(**config)

dbcursor = db.cursor()
dbcursor.execute("SELECT count FROM counter LIMIT 1")
count = dbcursor.fetchone()

print ('mon test donne {}'.format(count))
