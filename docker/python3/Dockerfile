FROM python:3.4-wheezy

MAINTAINER wielki.borsuk@gmail.com

RUN apt-get -q update && \
    apt-get -q install -y \
        wkhtmltopdf \
        git-core \
        xvfb \
        && rm -rf /var/lib/apt/lists/*

COPY wkhtmltopdf.sh /usr/bin/wkhtmltopdf.sh

RUN ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf

RUN pip install pdfkit flask pyjade

