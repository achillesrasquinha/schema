# schema
> 🔖 Metadata, for humans.

![https://travis-ci.org/achillesrasquinha/schema](https://img.shields.io/travis/achillesrasquinha/schema.svg?style=flat-square)
![https://saythanks.io/to/achillesrasquinha](https://img.shields.io/badge/Say%20Thanks-🦉-1EAEDB.svg?style=flat-square)
![https://paypal.me/achillesrasquinha](https://img.shields.io/badge/donate-💵-f44336.svg?style=flat-square)

<p align="justify">
    <b>schema</b> keeps it simple by fetching you human-readable (and minimal) schemas from data <a href="models">models</a> (provided by <a href="http://schema.org">schema.org</a>) updated <a href="https://en.wikipedia.org/wiki/Daily_build">nightly</a>. This ensures that you optionally recieve up-to-date schemas (<em>on the fly</em>) without having <b>schema</b> reinstalled, and speak in the same language with other users too.
</p>

```python
>>> import schema
>>> thing = schema.Schema('Thing', dict(url = 'http://bit.ly/2fbwx4m'))
```