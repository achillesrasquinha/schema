# imports - standard imports
import os
import json

# imports - third-party imports
import requests

def parse_tree(data, core = False):
    tree = dict()
    
    for key, value in data.items():
        if not key.startswith('@'):
            if   key == 'name':
                tree['name']     = value
            elif key == 'description':
                tree['desc']     = value
            elif key == 'layer':
                tree['type']     = value
            elif key == 'children':
                tree['children'] = [parse_tree(child, core = core) for child in value]

    return tree

def get_tree(core = False):
    response = requests.get('http://schema.org/docs/tree.jsonld')
    if  response.ok:
        data = response.json()
        tree = parse_tree(data, core = core)

        return tree
    else:
        response.raise_for_status()

class SchemaBot(object):
    def __init__(self):
        pass

    def run(self, core = False, savedir = '.', indent = 4):
        dirpath = os.path.abspath(savedir)

        tree    = get_tree(core = core)

        with open(os.path.join(dirpath, 'tree.json'), mode = 'w') as f:
            json.dump(tree, f, indent = indent)