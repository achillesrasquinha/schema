# imports - compatibility imports
from __future__          import absolute_import

# imports - module imports
from schema.util.checker import check_str, check_mapping

class Checker(object):
    def __init__(self):
        self.cache = Cache()
        self.cache.create()

    def check(self, name, props, raise_err = False, refresh = False, verbose = False):
        check_str(name, raise_err = raise_err)
        check_mapping(props, raise_err = raise_err)

        meta = self.cache.get(name, refresh = refresh, verbose = verbose)

