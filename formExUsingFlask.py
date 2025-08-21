from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__)

# What is request in Flask?
# 👉 Definition:
# request is an object in Flask (imported from flask) that contains all the data sent by the client (browser, API request, etc.) to the server.
# It includes things like form data, query parameters, headers, cookies, and request method (GET/POST).
# 👉 Explanation:
# Every time a client sends an HTTP request, Flask makes it available via the request object.
@app.route('/data', methods=['GET','POST'])
def data():
    return f'Request method used: {request.method}'

# How do you get query parameters (request.args) and form data (request.form)?
# 👉 Definition:
# request.args: Used to fetch query string parameters (from URL, e.g., /search?name=John&age=25).
# request.form: Used to fetch form data submitted using POST method (from an HTML form).
@app.route('/search')
def search():
    name = request.args.get('name')
    age = request.args.get('age')
    return f'Query params -> Name: {name}, Age: {age}'

@app.route('/submit', methods=['POSt'])
def submit():
    username = request.form['username']
    password = request.form['password']
    return f'form data -> username: {username}, password: {password}'

# how do you return json in flask?
# flask provides a helper function jsonify() to return json data as a proper HTTp response
@app.route('/json')
def json_data():
    data={'name': 'alice', 'age':30, 'city':'New York'}
    return jsonify(data)

# difference bertween request.args and request.form?
# request.args is used to access query parameters from the URL (GET requests).
# request.form is used to access form data submitted via POST requests.
@app.route('/text', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return f'Get param: {request.args.get('name')}'
    if request.method == 'POST':
        return f'Post params: {request.form['username']}'

# set and read cookies:
# request.cookies: reads cookies sent from the browser.
# response.set_cookie(): sets a cookie in the browser via response obj.
@app.route('/setcookie')
def set_cookie():
    resp = make_response('Cookie is set')
    resp.set_cookie('username', 'Alice')
    return resp

@app.route('/getcookie')
def get_cookie():
    username = request.cookies.get('username')
    if username:
        return f'Cookie value: {username}'
    else:
        return 'No cookie found'

if __name__ == '__main__':
    app.run(debug=True)