# How do you use templates in Flask?
    # In falsk we use seperate python logic(backend) and html(frontend) by using templates.
    # Templates are HTML files with placeholders for dynamic content.
    # Flask uses Jinja2 templating engine to render these templates.
    # flask provides a function render_template() to load and render HTM files.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Flask Home page')

@app.route('/profile')
def profile():
    return render_template('index.html', name='John Doe', age=30, title='Profile Page')

# dynamic data inside html template:
@app.route('/user/<username>')
def user_profile(username):
    return render_template('profile.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)