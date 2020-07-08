"""
CREATE TABLE sensor (
no int(11) not null auto_increment,
id varchar(10) not null,
temp varchar(10) not null,
date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
primary key(id)
)

"""

from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response

import pymysql
app = Flask(__name__)


import pymysql
 
conn = pymysql.connect(host='localhost', user='tester', password='1234',
                       db='sensordb', charset='utf8')
 
curs = conn.cursor()
sql = """insert into sensor(no, id,temp,date)
         values (NULL, %s, %s, NOW() )"""

@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        
        string  = json.dumps(request.data)
        print string
        data = json.loads(request.data)

        curs.execute(sql, (data['id'], data['key1']) )
        conn.commit()

        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)