#!/usr/bin/env python3

import pdfkit
import os


def main():
    path = os.path.expanduser('~/google_homepage.pdf')
    pdfkit.from_url('http://google.com', path)


if __name__ == "__main__":
    main()
