======================
``batlock666.example``
======================

An example package.

.. contents::


Usage
=====

Use the function ``hello`` to create a message::

    >>> from batlock666.example import hello
    >>> hello()
    'Hello, World!'
    >>> hello("Joe")
    'Hello, Joe!'


Scripts
=======

Use the script ``hello`` to display a message::

    $ hello
    Hello, World!
    $ hello Joe
    Hello, Joe!


Tests
=====

Use the following command to run the tests::

    $ python -m unittest
