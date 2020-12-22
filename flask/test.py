# THE WEB CONTAINER
# pip install flask flask-sqlalchemy


from flask import Flask, render_template, request
import mysql.connector
from datetime import datetime

app = Flask(__name__)

now = datetime.now()
connection = mysql.connector.connect(
    host="mysql",
    user="CICDUs",
    passwd="CICDPRO123",
    database='CICDPro'
)
query = connection.cursor(buffered=True)


def send(sequel, val):
    query.execute(sequel, val)
    connection.commit()
    print(query.rowcount, "record inserted.")


try:
    send("SELECT * FROM input", "")
except:
    send("CREATE TABLE input( ID INT AUTO_INCREMENT, input VARCHAR(100), DateUsed VARCHAR(100), PRIMARY KEY (id))", "")
    send("CREATE TABLE colors( ID INT AUTO_INCREMENT, ColorLeft VARCHAR(100), ColorRight VARCHAR(100), "
         "DateUsed VARCHAR(100), PRIMARY KEY (id))", "")


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/data', methods=['POST'])
def sql():
    data = request.get_json()
    if data['type'] == 'colors':
        left = data['color_left']
        right = data['color_right']
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        sequel = "INSERT INTO colors(ColorLeft, ColorRight, DateUsed) VALUES (%s, %s, %s)"
        val = (left, right, date_time)
        send(sequel, val)
        print(sequel, val)
    else:
        value = data['value']
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        sequel = "INSERT INTO input(input, DateUsed) VALUES (%s, %s)"
        val = (value, date_time)
        send(sequel, val)
        print(sequel, val)
    return data


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
