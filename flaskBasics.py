# What is flask? why is it called a micro framework?
    # falsk is a lightweight pyhton web framework from pallets project
    # built with werkzeug for http and jinja2 for tempalting
    #it is called micro because the core is small and unopinionated: routing, response/request, templates and almost nothing else.

# simple ex:
from flask import Flask

app = Flask(__name__)

# it is a decoator to define a route that maps between url and a python function
# when user visits that url in the browser, flask executes the corresponding function and return the response
@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)  # debug=True enables debug mode for development

# what is  role of app.run():
# starts flask builtin development server(werkzeug)
# it runs the event loop andlistens for http requests
# not  for production - use a real WSGI/ASGI server (eg: gunicorn, uWsgi, waitress
# common args: debug,host, port use_reloader

# what is flask(__name__)? why do we pass __name__?:
# Flask(import_name) needs to know where your application lives so it can:
# Set app.root_path (locate templates/, static/, instance folder).
# Build correct paths for error pages, logging, etc.
# Passing __name__ gives Flask the current module/package name, which resolves the correct filesystem location even if your app is imported from elsewhere.
