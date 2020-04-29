"""
This file is used by pip to install the package.

Reference: https://github.com/pypa/sampleproject/blob/master/setup.py
"""

from setuptools import setup
from os import path

import match

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    read_me = f.read()

setup(
    name="match",
    version=match.__version__,
    description="Check if a regular expression matches a string of text, using Thompson's Construction Algorithm.",
    long_description=read_me,
    long_description_content_type='text/markdown',
    url="https://github.com/daniel-keogh/graph-theory",
    author=match.__author__,
    license=match.__license__,
    packages=["match"],
    entry_points={
        "console_scripts": [
            "match=match.__main__:main",
        ]
    }
)
