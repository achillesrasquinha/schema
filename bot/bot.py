# imports - third-party imports
import requests

class SchemaBot(object):
    def __init__(self):
        pass

    def run(self):
        response = requests.get('http://schema.org/docs/tree.jsonld')
        if  response.ok:
            meta = response.json()
            
        else:
            response.raise_for_status()