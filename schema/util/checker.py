# imports - compatibility imports
import six

# imports - standard imports
from collections import Mapping

# imports - module imports
from schema.error import raise_type_error
from schema.util  import get_type_name

def check_type(instance, expected, raise_err = False, expected_name = None):
    if not isinstance(instance, expected):
        if raise_err:
            raise_type_error(
                expected = expected_name,
                recieved = get_type_name(instance)
            )
        else:
            return False
    else:
        return True

def check_str(instance, raise_err = True):
    check_type(instance, six.string_types, raise_err = raise_err, expected_name = 'str')

def check_mapping(instance, raise_err = True):
    check_type(instance, Mapping, raise_err = raise_err, expected_name = 'dict-like')