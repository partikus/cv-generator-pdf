# CV rendering module

planned as a part of CV management system, this module takes employee information as an input and returns the printout, either as html or pdf

## Setup

To start using, create a virtualenv for python, suggested way to do that:

```python3 -mvenv local
. local/bin/activate
```

Then in the virtualenv:

`pip install -r requirements.txt`

### PDF format requirements

To use pdf export you need `wkhtmltopdf` binary in your system
On Ubuntu this would be done with:

`apt-get install wkhtmltopdf`


## Docker

Alternatively you can just use docker definitions to run the application.

For an idea how to exactly, see `docker.sh`

