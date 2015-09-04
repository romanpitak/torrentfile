# -*- coding: utf-8 -*-

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='torrentfile',
    version='0.0.0',
    description='Torrent file parser.',
    long_description=readme(),
    url='https://github.com/romanpitak/torrentfile',
    author='Roman Piták',
    author_email='roman@pitak.net',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='torrent',
    packages=['torrentfile'],
    zip_safe=False,
)
