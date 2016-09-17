import json
import tempfile
from pdfkit import from_string
from flask import render_template


def render_html(template_name, json_model):
    model = json.loads(json_model)
    return render_template(template_name, model=model)


def render_pdf(template_name, json_model):
    (handle, path) = tempfile.mkstemp(prefix='cv-generator')
    html_view = render_html(template_name, json_model)
    from_string(html_view, path)

    return path
