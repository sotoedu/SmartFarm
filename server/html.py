from flask import Flask, url_for , request , json , Response , jsonify, render_template 
import pymysql
# import pygal
import time

app = Flask(__name__)

# MySQL Connection 
conn = pymysql.connect(host='localhost', user='tester', password='1234',
                       db='sensordb', charset='utf8')
 
curs = conn.cursor()
 
@app.route('/showdb', methods = ['GET'])
def api_message():
    sql="select * from sensor"

    html="""<html><table border="1"><tr><th>Index</th><th>ID</th><th>Temperature</th><th>Date</th></tr>"""
    curs.execute(sql)
    for row in curs.fetchall() :
        html += "<tr>"
        html += "<td>{}</td>".format(row[0])
        html += "<td>{}</td>".format(row[1])
        html += "<td>{}</td>".format(row[2])
        html += "<td>{}</td>".format(row[3])
        print (row[0], " ", row[1], " ", row[2], " ", row[3])
        html += "</tr>"
    html += "</table>"
    html += "</html>"
    return 	html


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)

