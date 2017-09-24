# imports - module imports
from schema.util.checker import check_url

class URL(object):
    def __init__(self, url):
        check_url(url, raise_err = True)

        self.url = url

    def __repr__(self):
        string   = self.url

        return string

    def __str__(self):
        string   = self.url

        return string