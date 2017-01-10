#!/usr/bin/env python
from setuptools import setup

requirements = []

long_description = ''
with open('./README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name='PyIntruder',
    version='0.1.1',
    py_modules=[
	'PyIntruder',
    ],
    install_requires=requirements,

    author='sirpsycho',
    author_email='',
    classifiers=[
	'Development Status :: 3 - Alpha',
	'Intended Audience :: Penetration Testers',
	'Topic :: Penetration Testing :: Web Applications',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    description='Command line URL fuzzer',
    license='MIT',
    long_description=long_description,
    keywords='pyintruder, http, fuzzer, url, scan',
    url='https://github.com/sirpsycho/PyIntruder',
)
