from flask import Flask,request

app = Flask(__name__)
import mysql.connector as conn
mydb = conn.connect(host = "localhost", user= "root", passwd= "Rakshanda@26")
cursor = mydb.cursor()

@app.route('/fetch', methods = ['GET'])
def fetch_data():
    cursor.execute("select * from tasksql.mysqltable")
    l =[]
    for i in cursor.fetchall():
        l.append(i)
    return l

if __name__ == '__main__':
    app.run(debug=True, port=5003)
