======================
``batlock666.example``
======================

An example package.

.. contents::


Development
===========

1. Create a virtual environment::

    $ python -m venv venv

2. Upgrade package ``pip``::

    $ venv/bin/pip install --upgrade pip

3. Install the dependencies::

    $ venv/bin/pip install -r requirements.txt

4. Install package ``batlock666.example`` in development mode::

    $ venv/bin/python setup.py develop


Tools
=====


``flake8``
----------

Enforce the code style guide::

    $ venv/bin/flake8
