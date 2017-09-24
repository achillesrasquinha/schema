# imports - compatibility imports
from __future__          import absolute_import

# imports - standard imports
import pprint
from collections         import MutableMapping

# imports - module imports
from schema.cache        import Cache
from schema.error        import raise_not_implemented_error
from schema.util.checker import check_str

class Schema(MutableMapping):
    def __init__(self, name, props = None, refresh = False, version = None, verbose = False):
        check_str(name, raise_err = True)

        if props  != None:
            check_mapping(props, raise_err = True)

        self.cache = Cache(version = version)
        self.cache.create()

        self.store = self.cache.get(name, refresh = refresh)
        self.name  = name
        
    def __getitem__(self, key):
        raise_not_implemented_error()

    def __setitem__(self, key, value):
        raise_not_implemented_error()

    def __delitem__(self, key):
        raise_not_implemented_error()

    def __len__(self):
        raise_not_implemented_error()

    def __iter__(self):
        raise_not_implemented_error()

    def __repr__(self, indent = 4):
        string = pprint.pformat(self.store, indent = indent)

        return string

    def __str__(self):
        string = '<Schema [{name}]>'.format(
            name = self.name
        )

        return string

    def update(self, *args, **kwargs):
        pass