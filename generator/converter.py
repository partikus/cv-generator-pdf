import json
import tempfile
from pdfkit import from_string
import jinja2


def render_wihtout_request(template_name, model):
    env = jinja2.Environment(
        loader=jinja2.PackageLoader('generator', 'templates'),
        extensions=['pyjade.ext.jinja.PyJadeExtension']
    )
    template = env.get_template(template_name)
    return template.render(model=model)


def render_html(template_name, json_model):
    model = json.loads(json_model)
    return render_wihtout_request(template_name, model)


def render_pdf(template_name, json_model):
    (handle, path) = tempfile.mkstemp(prefix='cv-generator')
    html_view = render_html(template_name, json_model)

    options = {
        'user-style-sheet': 'generator/static/css/main.css'
    }

    from_string(html_view, path, options=options)

    return path
