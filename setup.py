#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for cookiecutter-fastapi."""

from setuptools import setup

__version__ = "0.0.1"

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-fastapi",
    version=__version__,
    description="A Cookiecutter template for creating FastAPI projects quickly.",
    long_description=long_description,
    author="Noel Wilson",
    author_email="jwnwilson@hotmail.co.uk",
    url="",
    download_url="",
    packages=[],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Framework :: FastAPI",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],
    keywords=(
        """
        cookiecutter, Python, projects, project templates, fastapi,
        skeleton, scaffolding, project directory, setup.py
        """
    ),
)