# imports - standard imports
import os

# imports - third-party imports
import pytest

# imports - module imports
from schema.util import (
    assign_if_none,
    get_type_name,
    get_uuid_str,
    makedirs
)

def test_assign_if_none():
    assert assign_if_none('foo', 'bar') == 'foo'
    assert assign_if_none(None , 'bar') == 'bar'

def test_get_type_name():
    assert get_type_name('foo') == 'str'
    assert get_type_name(12345) == 'int'
    assert get_type_name(dict ) == 'type'
    assert get_type_name(type ) == 'type'

def test_get_uuid_str():
    assert len(get_uuid_str())             == 36
    assert len(get_uuid_str(strip = True)) == 32

def test_makedirs():
    tempdirs = os.path.join(get_uuid_str(strip = True), get_uuid_str(strip = True))

    makedirs(tempdirs)
    assert os.path.exists(tempdirs) == True

    makedirs(tempdirs, exists_ok = True)
    assert os.path.exists(tempdirs) == True

    with pytest.raises(OSError):
        makedirs(tempdirs)

    os.removedirs(tempdirs)
