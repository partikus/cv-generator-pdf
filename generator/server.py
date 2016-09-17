from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from generator.util.dummy_data import dummy_employee
from generator import converter
import os


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
    return converter.render_html('dummy.jade', request.data.decode())


@app.route('/print/pdf', methods=['POST'])
def pdf():
    output_file = converter.render_pdf('dummy.jade', request.data.decode())
    return app.send_static_file(output_file)


def run(debug=True, host='0.0.0.0', port=5000):
    # this ensures that server refreshes the jade view
    directory = 'generator/templates'
    template_files = [os.path.join(directory, f) for f in os.listdir(directory)]

    app.run(host, port, debug, extra_files=template_files)


if __name__ == "__main__":
    run()
