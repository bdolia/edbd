#!/usr/bin/env python

from os import path
from setuptools import setup


wd = path.abspath(path.dirname(__file__))
with open(path.join(wd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    description = 'A text encryptor and decryptor that use a text file as a key.',
    name = 'edbd',
    version = '0.0.1',
    author = 'Bogdan Dolia',
    author_email = 'cr.co.erph@gmail.com',
    license='GNU General Public License v3.0',
    url = 'https://github.com/bdolia/edbd',
    download_url = 'https://github.com/bdolia/edbd/archive/0.0.1.tar.gz',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords = ['encrypt', 'decrypt'],
    packages = ['edbd']
)