# NOQA: D100

import os

from setuptools import find_packages
from setuptools import setup


def read_file(*paths):
    """Read a file.
    """
    with open(os.path.join(os.path.dirname(__file__), *paths)) as filehandle:
        return filehandle.read()


setup(
    name="batlock666.example",
    version="0.1.0",
    description="An example project.",
    long_description="\n".join([
        read_file("README.rst"),
        read_file("CONTRIBUTING.rst"),
        read_file("LICENSE.rst"),
        read_file("CHANGELOG.rst"),
    ]),
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",  # NOQA: E501
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["batlock666", "example"],
    author="Bert Vanderbauwhede",
    author_email="batlock666@gmail.com",
    url="https://github.com/batlock666/batlock666.example",
    license="GPL-3.0-or-later",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    zip_safe=False,
    install_requires=[],
    entry_points={
        "console_scripts": ["hello=batlock666.example.scripts:hello"],
    },
)
