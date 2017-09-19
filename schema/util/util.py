# imports - standard imports
import os

def makedirs(dirs, exists_ok = False):
    try:
        os.makedirs(dirs)
    except OSError as e:
        if not exists_ok:
            raise e

def assign_if_none(a, b):
    if a == None:
        a = b

    return a

def get_type_name(instance):
    type_ = type(instance)
    name  = type_.__name__

    return name