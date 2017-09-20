# imports - standard imports
import uuid

def get_uuid_str(strip = True):
    objekt = uuid.uuid4()
    string = str(objekt)

    if strip:
        string = string.replace('-', '')

    return string