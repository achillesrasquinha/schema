schema
======
    🔖 *"Metadata, for humans."*

Release: v\ |version| (:ref:`Installation <installation>`)

.. image:: https://img.shields.io/travis/achillesrasquinha/schema.svg?style=flat-square
    :target: https://travis-ci.org/achillesrasquinha/schema
.. image:: https://img.shields.io/badge/Say%20Thanks-🦉-1EAEDB.svg?style=flat-square
    :target: https://saythanks.io/to/achillesrasquinha
.. image:: https://img.shields.io/badge/donate-💵-f44336.svg?style=flat-square
    :target: https://paypal.me/achillesrasquinha

**schema** keeps it simple by fetching you human-readable (and minimal) schemas from data models (provided by `schema.org <http://schema.org>`_) updated **nightly**. This ensures that you optionally recieve up-to-date schemas (*on the fly*) without having **schema** reinstalled, and speak in the same language with other users too.

.. code:: python

    >>> import schema
    >>> thing = schema.Schema('Thing', dict(url = 'http://bit.ly/2fbwx4m'))

**schema** officially supports Python 2.7+ and 3.3+.

**schema** is created and currently maintained by `Achilles Rasquinha <https://github.com/achillesrasquinha>`_.