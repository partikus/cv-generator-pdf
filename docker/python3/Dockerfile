FROM python:3.4-wheezy

MAINTAINER wielki.borsuk@gmail.com

RUN apt-get -q update && \
    apt-get -q install -y \
        wkhtmltopdf \
        git-core \
        xvfb \
        gdebi \
        && wget http://download.gna.org/wkhtmltopdf/0.12/0.12.2/wkhtmltox-0.12.2_linux-wheezy-amd64.deb \
        && gdebi -n wkhtmltox-0.12.2_linux-wheezy-amd64.deb \
        && rm -rf /var/lib/apt/lists/*

RUN pip install pdfkit flask pyjade beanstalkc3 PyYaml
