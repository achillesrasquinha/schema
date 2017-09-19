# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import os
import json

# imports - third-party imports
import requests

# imports - module imports
from schema.util import assign_if_none, makedirs

class Cache(object):
    def __init__(self, location = None, dirname = None):
        self.location = assign_if_none(location, os.path.expanduser('~'))
        self.dirname  = assign_if_none(dirname,  '.schema')

    def create(self, exists_ok = True, refresh = False, indent = 4):
        basepath = os.path.join(self.location, self.dirname)
        metapath = os.path.join(basepath, 'models')

        makedirs(metapath, exists_ok = exists_ok)

        treepath = os.path.join(metapath, 'tree.json')
        if not os.path.exists(treepath) or refresh:
            response = requests.get('https://cdn.rawgit.com/achillesrasquinha/schema/dev/models/tree.json')
            if  response.ok:
                tree = response.json()

                with open(treepath, mode = 'w') as f:
                    json.dump(tree, f, indent = indent)
            else:
                response.raise_for_status()