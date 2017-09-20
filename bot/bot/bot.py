# imports - standard imports
import warnings

# imports - third-party imports
import requests

class SchemaBot(object):
    def run(self):
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
                            pass

                        klass.append(meta)
                        
                    elif node['@type'] == 'rdf:Property':
                        meta         = dict()
                        meta['name'] = node['rdfs:label']
                        meta['desc'] = node['rdfs:comment'] if 'rdfs:comment' in node else ""

                        if 'http://schema.org/domainIncludes' in node:
                            domains        = node['http://schema.org/domainIncludes']
                            meta['memb']   = [ ]

                            if   isinstance(domains, dict):
                                domain     = domain['@id'].replace('http://schema.org/', '')
                                meta['memb'].append(domain)
                            elif isinstance(domains, list):
                                for d in domains:
                                    domain = d['@id'].replace('http://schema.org/', '')
                                    meta['memb'].append(domain)
                            else:
                                warnings.warn('Unknown type {type_} for domains {domains}'.format(
                                    type_   = type(domains)
                                    domains = domains
                                ))
                        
                        props.append(meta)
        else:
            response.raise_for_status()
