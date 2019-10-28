# coding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route("/test_page")
def hello():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()