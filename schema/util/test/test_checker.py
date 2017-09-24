# imports - standard imports
import pytest

# imports - third-party imports
from schema.util.checker import (
    check_type,
    check_str,
    check_mapping
)

def test_check_type():
    assert check_type('foo', str ) == True
    assert check_type(12345, int ) == True
    assert check_type(list , type) == True

    assert check_type(12345, str)  == False
    assert check_type([123], dict) == False
    assert check_type(type , list) == False

    assert check_type('foo', str , raise_err = True) == True
    assert check_type(12345, int , raise_err = True) == True
    assert check_type(list , type, raise_err = True) == True

    with pytest.raises(TypeError):
        assert check_type(12345, str , raise_err = True, expected_name = 'str')
        assert check_type([123], dict, raise_err = True, expected_name = 'list')

def test_check_str():
    assert check_str('foo') == True
    assert check_str("bar") == True
    assert all(check_str('foo', "bar")) == True
    assert any(check_str('foo', 12345)) == True

    assert check_str(12345) == False
    assert check_str([123]) == False
    assert all(check_str(12345, [123])) == False

    assert check_str('foo', raise_err = True) == True
    assert check_str("bar", raise_err = True) == True
    assert all(check_str('foo', "bar", raise_err = True)) == True

    with pytest.raises(TypeError):
        check_str(12345, raise_err = True)
        check_str([123], raise_err = True)
        check_str("foo", [123], raise_err = True)
        check_str(12345, [123], raise_err = True)

def test_check_mapping():
    assert check_mapping({    }) == True
    assert check_mapping(dict()) == True
    assert all(check_mapping(dict(), { })) == True
    assert any(check_mapping(dict(), 123)) == True

    assert check_mapping('foo')  == False
    assert check_mapping(12345)  == False
    assert all(check_mapping('foo', 12345)) == False

    assert check_mapping({    }, raise_err = True) == True
    assert check_mapping(dict(), raise_err = True) == True
    assert all(check_mapping(dict(), { }, raise_err = True)) == True
    
    with pytest.raises(TypeError):
        check_mapping('foo', raise_err = True)
        check_mapping(12345, raise_err = True)
        check_mapping({   }, 12345, raise_err = True)
        check_mapping('foo', 12345, raise_err = True)