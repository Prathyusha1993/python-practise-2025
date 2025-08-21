
from flask import Flask, request, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Homepage!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Form submitted using post method!'
    else:
        return 'login page opened using GET method!'

# handle multiple riutes with same function
@app.route('/about', methods=['GET'])
@app.route('/info', methods=['GET'])
def about():
    return 'This is the about page! You can also access it via /info.'

# pass a varibale in route
@app.route('/user/<username>', methods=['GET', 'POST'])
def profile(username):
    return f'Hello, {username}! This is your profile page.'

# we can also define variable types in the riute for dynamic routing
@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    return f'Post ID: {post_id}'

# what is url_for() and why is it used?
# url_for() is a Flask function that generates a URL to the given endpoint with the provided arguments.
# It is used to create URLs dynamically, which helps avoid hardcoding URLs in templates or code.

@app.route('/contact')
def contact_page():
    return 'contact page'

@app.route('/go')
def go():
    return f'Go to: {url_for('contact_page')}'






if __name__ == '__main__':
    app.run(debug=True)