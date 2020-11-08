#!/usr/bin/env python3

from os.path import join, dirname
from setuptools import setup

requirements = open(join(dirname(__file__), 'requirements.txt')).readlines()

setup(
    name='BDO_app',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'BDO_app=BDO_app.__main__:run'
        ]
    }
)
