from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        # Get query params ?name=Prathyusha&age=25
        name = request.args.get('name')
        age = request.args.get('age')
        return f'Get params: Name: {name}, Age: {age}'
    elif request.method == 'POST':
        # Get form data from HTML form
        name = request.form.get('name')
        age = request.form.get('age')

        # Example: Setting a cookie
        response = make_response(f'POST request -> Name: {name}, Age: {age}')
        response.set_cookie('username', name)
        return response

@app.route('/profile')
def profile():
    username = request.cookies.get('username')
    if username:
        return f'Hello, {username}! This is your profile page.'
    else:
        return 'No cookie found, please submit the form first.'

# JSON response example
@app.route('/json')
def json_response():
    data = {"message": "Hello Flask", "status": "success"}
    return jsonify(data)





if __name__ == '__main__':
    app.run(debug=True)