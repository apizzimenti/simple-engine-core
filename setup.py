#!/usr/bin/env python3

from setuptools import setup

setup(
    name="simple-engine-core",
    description="Reads in HTML, reads out JSON",
    long_description=open("README.md").read(),

    license="MIT",
    version=2.3,

    url="https://github.com/apizzimenti/simple-engine-core.git",
    author="Anthony Pizzimenti",
    author_email="pizzimentianthony@gmail.com",

    packages=["core", "core.interpreter", "core.tools"],

    entry_points={
        "console_scripts": ["engine=core.index:main"],
    },

    install_requires=[
        "beautifulsoup4"
    ]
)
