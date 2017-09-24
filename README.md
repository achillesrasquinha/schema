<div align="center">
    <img src=".github/logo.png" width="256">
    <h1>schema</h1>
    <h4>metadata, for humans</h4>
</div>

<div align="center">
    <a href="https://travis-ci.org/achillesrasquinha/schema">
        <img src="https://img.shields.io/travis/achillesrasquinha/schema.svg">
    </a>
    <a href="https://saythanks.io/to/achillesrasquinha">
        <img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg">
    </a>
    <a href="https://paypal.me/achillesrasquinha">
        <img src="https://img.shields.io/badge/donate-%24-f44336.svg">
    </a>
</div>

<p align="justify">
    <b>schema</b> helps you create objects, <em>on the fly</em>.
</p>

### Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [License](#license)

#### Installation

To install **schema**, simply use [`pip`](https://pip.pypa.io):

```console
$ pip install schemapy
```

#### Usage

<p align="justify">
    <b>schema</b> keeps it simple by fetching you human-readable (and minimal) schemas from data <a href="models">models</a> (provided by <a href="http://schema.org">schema.org</a>) updated <a href="https://en.wikipedia.org/wiki/Daily_build">nightly</a>. This ensures that you optionally recieve up-to-date schemas (<em>on the fly</em>) without having <b>schema</b> reinstalled, and speak in the same language with other users too.
</p>

```python
>>> import schema
>>> thing = schema.Schema('Thing', dict(url = 'http://bit.ly/2fbwx4m'))
```

##### Seamless Object-Relational Mapping (TODO)
```python
>>> db = schema.DB('sqlite', 'foo.db')
>>> db.insert(thing)
```

#### Features
* Support for Python **2.7+** and **3.3+**

#### License
This repository has been released under the [MIT License](LICENSE)