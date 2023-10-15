from flask import Flask,request,jsonify

app = Flask(__name__)

import mysql.connector as conn

@app.route('/get_data')
def get_data():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try :
        con1 = conn.connect(host="localhost", user="root", passwd="Rakshanda@26", database =db)
        cursor = con1.cursor(dictionary=True)
        cursor.execute(f"select * from {tn}")
        data = cursor.fetchall()
        con1.commit()
        con1.close()

    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
