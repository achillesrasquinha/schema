# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import os
import json

# imports - third-party imports
import requests

# imports - module imports
from schema.error        import SchemaError
from schema.util         import assign_if_none, makedirs
from schema.util.checker import check_str

class Cache(object):
    def __init__(self, location = None, dirname = None, version = None):
        if location != None:
            check_str(location, raise_err = True)
        if dirname  != None:
            check_str(dirname , raise_err = True)
        if version  != None:
            check_str(version , raise_err = True)

        self.location = assign_if_none(location, os.path.expanduser('~'))
        self.dirname  = assign_if_none(dirname , '.schema')
        self.version  = assign_if_none(version , 'dev')

    def create(self, exists_ok = True):
        self.basepath = os.path.join(self.location, self.dirname)
        self.metapath = os.path.join(self.basepath, 'models')

        makedirs(self.metapath, exists_ok = exists_ok)

    def get(self, name, refresh = False, verbose = False):
        typepath      = os.path.join(self.metapath, name)

        if not os.path.exists(typepath) or refresh:
            response  = requests.get('https://cdn.rawgit.com/achillesrasquinha/schema/{version}/models/{name}.json'.format(
                version = self.version,
                name    = name
            ))
            
            if response.ok:
                data = response.json()

                with open(typepath, mode = 'w') as f:
                    json.dump(data, f)
            else:
                if response.status_code == 404:
                    raise SchemaError('Schema {name} not found.'.format(name = name))
                else:
                    response.raise_for_status()
        else:
            with open(typepath, mode = 'r') as f:
                data = json.load(f)

        return data

    def all(self):
        pass