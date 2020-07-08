from flask import Flask, url_for , request , json , Response , jsonify 
import logging
app = Flask(__name__)
file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

@app.route('/hello')
def api_hello():
    print (request.args)
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello SotoLAB'

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"
                                                                

@app.route('/messages', methods = ['POST'])
def api_message():

#    print ("!!!message!!!")
#    print(request.data)
#    print(json.dumps(request.data))

    if request.headers['Content-Type'] == 'text/plain':
        print ("text/plain")
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        print("Json type", json.dumps(request.json))
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"
    else:
        return "415 Unsupported Media Type ;)"


@app.route('/helloworld', methods = ['GET'])
def api_helloworld():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://localhost'

    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/users/<userid>', methods = ['GET'])
def api_users(userid):
    users = {'1':'john', '2':'steve', '3':'bill'}
    
    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()


@app.route('/hellolog', methods = ['GET'])
def api_hellolog():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.error('screaming bloody murder!')
    
    return "check your logs\n"

if __name__ == '__main__':
    app.run(host='localhost',port=3000)

