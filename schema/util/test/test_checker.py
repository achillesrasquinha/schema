# imports - standard imports
import pytest

# imports - third-party imports
from schema.util.checker import (
    check_type,
    check_str,
    check_mapping
)

def test_check_type():
    assert check_type('foo', str) == True
    assert check_type(12345, int) == True
    assert check_type(12345, str) == False

    with pytest.raises(TypeError):
        assert check_type(12345, str, raise_err = True, expected_name = 'str')

def test_check_str():
    assert check_str('foo') == True
    assert check_str(12345) == False

    with pytest.raises(TypeError):
        assert check_str(12345, raise_err = True)

def test_check_mapping():
    assert check_mapping({   }) == True
    assert check_mapping('foo') == False

    with pytest.raises(TypeError):
        assert check_mapping(12345, raise_err = True)