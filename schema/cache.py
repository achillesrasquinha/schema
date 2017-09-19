# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import os
import json

# imports - third-party imports
import requests

# imports - module imports
from schema.error import SchemaError
from schema.util  import assign_if_none, makedirs

class Cache(object):
    def __init__(self, location = None, dirname = None):
        self.location = assign_if_none(location, os.path.expanduser('~'))
        self.dirname  = assign_if_none(dirname,  '.schema')

    def create(self, exists_ok = True, refresh = False, indent = 4):
        self.basepath = os.path.join(self.location, self.dirname)
        self.metapath = os.path.join(self.basepath, 'models')

        makedirs(self.metapath, exists_ok = exists_ok)

        self.treepath = os.path.join(self.metapath, 'tree.json')
        if not os.path.exists(self.treepath) or refresh:
            response = requests.get('https://cdn.rawgit.com/achillesrasquinha/schema/dev/models/tree.json')
            if  response.ok:
                tree = response.json()

                with open(treepath, mode = 'w') as f:
                    json.dump(tree, f, indent = indent)
            else:
                response.raise_for_status()

    def get(self, type_, refresh = False):
        typepath = os.path.join(self.metapath, type_)
        if not os.path.exists(typepath) or refresh:
            response = requests.get('https://cdn.rawgit.com/achillesrasquinha/schema/dev/models/{type_}.json'.format(type_ = type_))
            if response.ok:
                data = response.json()

                with open(typepath, mode = 'r') as f:
                    json.dump(data, f)
            else:
                if response.status_code == 404:
                    raise SchemaError('Schema {type_} not found.'.format(type_ = type_))
                else:
                    response.raise_for_status()
        else:
            with open(typepath, mode = 'r') as f:
                data = json.load(f)

        return data