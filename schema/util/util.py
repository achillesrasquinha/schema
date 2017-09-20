# imports - standard imports
import os
import uuid

def assign_if_none(a, b):
    if a == None:
        a = b

    return a

def get_type_name(instance):
    type_ = type(instance)
    name  = type_.__name__

    return name

def get_uuid_str(strip = False):
    objekt = uuid.uuid4()
    string = str(objekt)
    
    if strip:
        string = string.replace('-', '')

    return string

def makedirs(dirs, exists_ok = False):
    try:
        os.makedirs(dirs)
    except OSError as e:
        if not exists_ok:
            raise e