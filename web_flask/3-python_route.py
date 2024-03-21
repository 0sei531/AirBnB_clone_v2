#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    """ Function that says Hello HBNB """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """ Function that says HBNB """
    return 'HBNB'

@app.route('/c/<text>')
def c_compliment(text):
    """ Display a message starting with C """
    message = text.replace('_', ' ')
    return 'C %s' % message

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_compliment(text):
    """ Display a message starting with Python """
    message = text.replace('_', ' ')
    return 'Python %s' % message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

