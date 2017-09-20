# imports - third-party imports
import pytest

# imports - module imports
from schema.error import (
    MESSAGES,
    raise_not_implemented_error,
    raise_type_error
)

def test_raise_not_implemented_error():
    with pytest.raises(NotImplementedError):
        raise_not_implemented_error()

def test_raise_type_error():
    with pytest.raises(TypeError) as e:
        raise_type_error(
            expected = 'foo',
            recieved = 'bar'
        )

        assert str(e) == MESSAGES.format(expected = 'foo', recieved = 'bar')
