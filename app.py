#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "For Banders Everywhere!"

if __name__ == '__main':
    app.run(debug=True)
