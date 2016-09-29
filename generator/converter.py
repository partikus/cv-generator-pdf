import json
import tempfile
from pdfkit import from_string
import jinja2
import datetime


def format_datetime(value, format='date'):
    if format == 'date':
        format = '%Y-%m-%d'
    elif format == 'month':
        format = '%Y-%m'

    if isinstance(value, str):
        value = value.split('+')[0]
        value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')

    return datetime.datetime.strftime(value, format)


def month_range(dummy, since=None, until=None):
    since = format_datetime(since, 'month') if since else 'Always'
    until = format_datetime(until, 'month') if until else 'Current'

    return '{} - {}'.format(since, until)


def render_wihtout_request(template_name, model):
    env = jinja2.Environment(
        loader=jinja2.PackageLoader('generator', 'templates'),
        extensions=['pyjade.ext.jinja.PyJadeExtension']
    )
    env.filters['months'] = format_datetime
    env.filters['month_range'] = month_range

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
