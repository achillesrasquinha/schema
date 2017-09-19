# imports - standard imports
import os
import json
import warnings
from collections import deque

# imports - third-party imports
import requests
from bs4 import BeautifulSoup

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

def save_data(tree, dirpath = '.', indent = 4):
    # Breadth-First-Search (Level-Order-Search)
    queue = deque()
    queue.append(tree)

    while len(queue):
        node = queue.popleft()
        meta = dict()
        meta['type'] = node['name']

        url  = 'http://schema.org/{name}'.format(name = meta['type'])
        res  = requests.get(url)
        if res.ok:
            html  = res.content
            soup  = BeautifulSoup(html, 'html.parser')

            for i, table in enumerate(soup.find_all('table', class_ = 'definition-table')):
                for j, tbody in enumerate(table.find_all('tbody')):
                    pass
            
            path = os.path.join(dirpath, '{type_}.json'.format(type_ = meta['type']))

            with open(path, mode = 'w') as f:
                json.dump(meta, f, indent = indent)
        else:
            response.raise_for_status()

        if 'children' in node:
            for child in node['children']:
                queue.append(child)

class SchemaBot(object):
    def __init__(self):
        pass

    def run(self, core = False, savedir = '.', indent = 4):
        dirpath = os.path.abspath(savedir)

        tree    = get_tree(core = core)

        with open(os.path.join(dirpath, 'tree.json'), mode = 'w') as f:
            json.dump(tree, f, indent = indent)

        save_data(tree, dirpath = dirpath, indent = indent)