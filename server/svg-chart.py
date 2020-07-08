# http://www.pygal.org/en/stable/documentation/

from flask import Flask, url_for , request , json , Response , jsonify, render_template 
import pymysql
import pygal
import time
import collections

app = Flask(__name__)

# MySQL Connection 
conn = pymysql.connect(host='localhost', user='tester', password='1234',
                       db='sensordb', charset='utf8')
 
curs = conn.cursor()
curs.execute("SELECT * FROM sensor")

rows = curs.fetchall()
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['no'] = int(row[0])
    d['id'] = row[1]
    d['temp'] = int(row[2])
    d['date'] = row[3]
    objects_list.append(d)

mark_list = [x['no'] for x in objects_list]
print mark_list

jsondata = json.dumps(objects_list)
print jsondata
 
# -------------------------------------------
# Charting route which displays the bar chart
# -------------------------------------------
 
@app.route("/bar")
def bar():
    chart = pygal.Bar()
#    chart = pygal.Line()
#    chart = pygal.Pie()

    mark_list = [x['temp'] for x in objects_list]
    chart.add('Temperature Score',mark_list)

    # tourn_list = [x['temp'] for x in objects_list]
    # chart.add('Humidity Score',tourn_list)

    chart.x_labels = [x['date'] for x in objects_list]
    chart.render_to_file('static/images/bar_chart0.svg')
    img_url_0 = 'static/images/bar_chart0.svg?cache=' + str(time.time())

    chart = pygal.Line()

    mark_list = [x['temp'] for x in objects_list]
    chart.add('Annual Mark List',mark_list)

    # tourn_list = [x['temp'] for x in objects_list]
    # chart.add('Tournament Score',tourn_list)

    chart.x_labels = [x['date'] for x in objects_list]
    chart.render_to_file('static/images/bar_chart1.svg')
    img_url_1 = 'static/images/bar_chart1.svg?cache=' + str(time.time())

    return render_template('app.html',image_url_0 = img_url_0, image_url_1 = img_url_1)

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

