# Explore the 'Flask' module and create a web server using Flask & Python.

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

