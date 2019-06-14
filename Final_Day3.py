from flask import *
from flask_basicauth import BasicAuth
import pymysql
import time
import requests

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'sdi'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'

secure_my_api = BasicAuth(app)

@app.route('/createUser', methods=['POST'])
@secure_my_api.required
def getBody():
    body =  request.get_json()
    user= body['username']
    password = body['password']
    connectDB(user, password)

    return "Success!!"

def connectDB(u, p):
    connect = pymysql.connect(host="203.154.83.124", port=3306, db="test_database", user="root", password="12345678")
    cursor = connect.cursor()  # access to edit database

    try:
        sql = "INSERT INTO users (username, password, create_time) VALUE(%s, %s, %s)"  # INSERT INTO [table name]
        value = (u, p, int(time.time()))

        cursor.execute(sql, value)
        connect.commit()
        connect.close()

        lineNoti(u)
    except Exception as error:
        print(error)
        connect.rollback()  # if error to insert every thing can insert is comeback
        connect.close()

def lineNoti(u):
    url = 'https://notify-api.line.me/api/notify'
    token = 'YdordyuCI0R0xXF71mzRxjwGlrGnRyjrSuajMWCIJyB'
    headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}
    msg = 'Created User : ' + str(u)
    r = requests.post(url, headers=headers, data={'message': msg})
    print(r.text)

app.run(host="0.0.0.0")