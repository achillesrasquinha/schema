# imports - compatibility imports
from __future__ import absolute_import

# imports - module imports
from schema.util import assign_if_none, makedirs

class Cache(object):
    def __init__(self, location = None, dirname = None):
        self.location = assign_if_none(location, os.path.expanduser('~'))
        self.dirname  = assign_if_none(dirname,  '.schema')

    def create():
        basepath = os.path.join(self.location, self.dirname)

        makedirs(basepath, exists_ok = True)