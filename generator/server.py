from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from generator.util.dummy_data import dummy_employee
import os
import json
from pdfkit import from_string


app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


@app.route('/')
def index():
    return url_for('static', filename='main.css')
    # return "hello"


@app.route('/dummy')
def dummy():
    model = dummy_employee()
    return render_template('dummy.jade', model=model)


@app.route('/echo', methods=['POST'])
def echo():
    return request.data.decode()


@app.route('/print/html', methods=['POST'])
def html():
    model = json.loads(request.data.decode())
    return render_template('dummy.jade', model=model)


@app.route('/print/pdf', methods=['POST'])
def pdf():
    model = json.loads(request.data.decode())
    output_file = '/tmp/output.pdf'
    from_string(render_template('dummy.jade', model=model), output_file)
    return app.send_static_file(output_file)


def run(debug=True, host='0.0.0.0', port=5000):
    # this ensures that server refreshes the jade view
    directory = 'generator/templates'
    template_files = [os.path.join(directory, f) for f in os.listdir(directory)]

    app.run(host, port, debug, extra_files=template_files)


if __name__ == "__main__":
    run()
