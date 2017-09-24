# imports - compatibility imports
from __future__          import absolute_import
from six                 import iteritems

# imports - module imports
from schema.error        import SchemaValidationError
from schema.cache        import Cache
from schema.util.checker import check_str, check_uint, check_mapping

class Checker(object):
    def __init__(self):
        self.cache = Cache()
        self.cache.create()

    def check(self, name, props, depth = None, raise_err = False, refresh = False, verbose = False):
        check_str(name, raise_err = True)
        check_mapping(props, raise_err = True)

        if depth != None:
            check_uint(depth, raise_err = True)

        meta = self.cache.get(name, refresh = refresh, verbose = verbose)

        for key, value in iteritems(props):
            for prop in meta['prop']:
                if key in prop['name']:
                    pass
            else:
                hasprop = False
                for _, pprops in iteritems(meta['from']):
                    for prop in pprops:
                        if key in prop['name']:
                            hasprop = True
                            break
                
                if not hasprop:
                    if raise_err:
                        raise SchemaValidationError('No such prop {key} found for schema {name}.'.format(
                            key  = key,
                            name = name
                        ))
                    else:
                        pass