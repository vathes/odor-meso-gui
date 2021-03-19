#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='odor-meso-gui',
    version='0.0.2',
    description='Simple GUI for odor recording for Reimer and Pfaffinger labs',
    author='Vathes',
    author_email='support@vathes.com',
    packages=find_packages(exclude=[]),
    install_requires=requirements,
)
