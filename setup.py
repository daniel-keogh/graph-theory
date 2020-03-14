"""
This file is used by pip to install the module.

Reference: https://github.com/pypa/sampleproject/blob/master/setup.py
"""

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    read_me = f.read()

setup(
    name="match",
    version="1.0.0",
    description="Check if a regular expression matches a string of text, using Thompson's Construction Algorithm.",
    long_description=read_me,
    long_description_content_type='text/markdown',
    url="https://github.com/daniel-keogh/graph-theory",
    author="Daniel Keogh",
    license="MIT",
    packages=["match"],
    entry_points={
        "console_scripts": [
            "match=match.__main__:main",
        ]
    }
)
