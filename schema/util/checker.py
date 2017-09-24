# imports - compatibility imports
import six
from six.moves.urllib.parse import urlparse

# imports - standard imports
from collections import Mapping

# imports - module imports
from schema.error import raise_type_error
from schema.util  import assign_if_none, get_type_name

# Primitive Checkers
def check_type(instance, expected, raise_err = False, expected_name = None):
    if not isinstance(instance, expected):
        if raise_err:
            raise_type_error(
                expected = assign_if_none(expected_name, type(expected)),
                recieved = get_type_name(instance)
            )
        else:
            return False
    else:
        return True

def check_uint(*isinstance, **kwargs):
    raise_err = assign_if_none(kwargs.get('raise_err'), False)
    bools     = [False] * len(instances)

    for i, instance in enumerate(instances):
        bools[i]  = check_type(instance, int, raise_err = raise_err)

        if instance < 0:
            if raise_err:
                raise ValueError('{number} is negative.')
            else:
                bools[i] &= False
        else:
            bools[i] &= True

    return bools[0] if len(instances) == 1 else bools

def check_uint16(*isinstances, **kwargs):
    raise_err = assign_if_none(kwargs.get('raise_err'), False)
    bools     = [False] * len(instances)

    for i, instance in enumerate(instances):
        bools[i]  = check_type(instance, int, raise_err = raise_err)
        bools[i] &= check_range(instance, 0, 65535, raise_err = raise_err)

    return bools[0] if len(instances) == 1 else bools

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

def check_range(number, min_, max_, raise_err = False):
    if min_ <= number <= max_:
        if raise_err:
            raise ValueError('{number} not in range [{min_}, {max_}).'.format(
                number = number,
                min_   = min_,
                max_   = max_
            ))
        else:
            return False
    else:
        return True

def check_url(*urls, **kwargs):
    check_str(*urls, **kwargs)

    raise_err = assign_if_none(kwargs.get('raise_err'), False)
    bools     = [False] * len(urls)

    for i, url in enumerate(urls):
        parse = urlparse(url)
        if parse.scheme:
            bools[i] = True
        else:
            if raise_err:
                raise ValueError('{url} not a valid URL.'.format(
                    url = url
                ))
            else:
                bools[i] = False
        
    return bools[0] if len(urls) == 1 else bools