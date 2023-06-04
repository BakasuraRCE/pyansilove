#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'pydantic>=1.10', 'pillow>=9.5']

test_requirements = []

setup(
    author="Bakasura",
    author_email='bakasura@protonmail.ch',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="Library for converting ANSI, ASCII, and other formats to PNG",
    entry_points={
        'console_scripts': [
            'pyansilove=pyansilove.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyansilove',
    name='pyansilove',
    packages=find_packages(include=['pyansilove', 'pyansilove.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/BakasuraRCE/pyansilove',
    version='1.4.1',
    zip_safe=False,
)
