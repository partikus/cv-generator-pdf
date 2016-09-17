from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "hello"


@app.route('/dummy')
def dummy():
    return render_template('dummy.html')


@app.route('/echo', methods=['POST'])
def echo():
    return request.data.decode()


def run(debug=True, host='0.0.0.0', port=5000):
    app.run(host, port, debug)


if __name__ == "__main__":
    run()
