# imports - compatibility imports
import six

# imports - standard imports
from collections import Mapping

# imports - module imports
from schema.error import raise_type_error
from schema.util  import assign_if_none, get_type_name

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

def check_str(*instances, **kwargs):
    raise_err = assign_if_none(kwargs.get('raise_err'), False)
    bools     = [False] * len(instances)

    for i, instance in enumerate(instances):
        bools[i] = check_type(instance, six.string_types, raise_err = raise_err, expected_name = 'str')

    return bools[0] if len(instances) == 1 else bools

def check_mapping(*instances, **kwargs):
    raise_err = assign_if_none(kwargs.get('raise_err'), False)
    bools     = [False] * len(instances)

    for i, instance in enumerate(instances):
        bools[i] = check_type(instance, Mapping, raise_err = raise_err, expected_name = 'dict-like')

    return bools[0] if len(instances) == 1 else bools