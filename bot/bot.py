# imports - standard imports
import os
import json
import warnings
from collections import deque

# imports - third-party imports
import requests
from tqdm import tqdm

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
        dirpath   = os.path.abspath(savedir)

        tree      = get_tree(core = core)

        with open(os.path.join(dirpath, 'tree.json'), mode = 'w') as f:
            json.dump(tree, f, indent = indent)

        response  = requests.get('http://schema.org/version/latest/schema.jsonld')
        if response.ok:
            data  = response.json()
            graph = data['@graph']
            klass = [ ]
            props = [ ]
            
            for node in graph:
                if 'rdfs:label' in node:
                    if   node['@type'] == 'rdfs:Class':
                        meta         = dict()
                        meta['name'] = node['rdfs:label']
                        meta['desc'] = node['rdfs:comment'] if 'rdfs:comment' in node else ""

                        if 'rdfs:subClassOf' in node:
                            sklass       = node['rdfs:subClassOf']
                            meta['from'] = [ ]
                            
                            if   isinstance(sklass, dict):
                                sklass   = sklass['@id'].replace('http://schema.org/', '')
                                meta['from'].append(sklass)
                            elif isinstance(sklass, list):
                                for s in sklass:
                                    s    = s['@id'].replace('http://schema.org/', '')
                                    meta['from'].append(s)

                        klass.append(meta)

                    elif node['@type'] == 'rdf:Property':
                        meta         = dict()
                        meta['name'] = node['rdfs:label']
                        meta['desc'] = node['rdfs:comment'] if 'rdfs:comment' in node else ""

                        if 'http://schema.org/domainIncludes' in node:
                            domains         = node['http://schema.org/domainIncludes']
                            meta['members'] = [ ]

                            if   isinstance(domains, dict):
                                domain      = domains['@id'].replace('http://schema.org/', '')
                                meta['members'].append(domain)
                                
                            elif isinstance(domains, list):
                                for d in domains:
                                    domain  = d['@id'].replace('http://schema.org/', '')
                                    meta['members'].append(domain)

                        if 'http://schema.org/rangeIncludes' in node:
                            types           = node['http://schema.org/rangeIncludes']
                            meta['type']    = [ ]

                            if   isinstance(types, dict):
                                tipe        = types['@id'].replace('http://schema.org/', '')
                                meta['type'].append(tipe)
                                
                            elif isinstance(types, list):
                                for t in types:
                                    tipe   = t['@id'].replace('http://schema.org/', '')
                                    meta['type'].append(tipe)

                        props.append(meta)

            classes = [ ]

            for k in klass:
                meta         = dict()
                meta['name'] = k['name']
                meta['prop'] = [ ]

                for prop in props:
                    if 'members' in prop and 'type' in prop:
                        if meta['name'] in prop['members']:
                            meta['prop'].append({
                                'name': prop['name'],
                                'desc': prop['desc'],
                                'type': [tipe for tipe in prop['type']]
                            })

                if 'from' in k:
                    meta['froms'] = k['from']

                classes.append(meta)

            for c in tqdm(classes):
                meta         = dict()
                meta['name'] = c['name']
                meta['prop'] = c['prop']

                meta['from'] = { }

                if 'froms' in c:
                    for klass in c['froms']:
                        for j in classes:
                            if j['name'] == klass:
                                meta['from'][klass] = [prop for prop in j['prop'] if 'prop' in j]

                with open(os.path.join(dirpath, '{name}.json'.format(name = meta['name'])), mode = 'w') as f:
                    json.dump(meta, f, indent = indent)
        else:
            response.raise_for_status()