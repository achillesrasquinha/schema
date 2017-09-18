# imports - third-party imports
import pytest

# imports - module imports
from schema.util import (
    assign_if_none,
    get_type_name
)

def test_assign_if_none():
    assert assign_if_none('foo', 'bar') == 'foo'
    assert assign_if_none(None,  'bar') == 'bar'

def test_get_type_name():
    assert get_type_name('foo') == 'str'
    assert get_type_name(12345) == 'int'