# imports - third-party imports
import pytest

# imports - module imports
from schema import Schema

def test_schema_str():
    name   = 'Thing'
    schema = Schema(name)

    assert str(schema) == '<Schema [{name}]>'.format(name = name)