# inspired by npm's package.json
# imports - standard imports
import os

# expose the __version__
with open('schema/__version__.py') as f:
    code = f.read()
    exec(code)

def get_long_description(*files):
    for f in files:
        pass

def get_dependencies(type_ = None, dirpath = 'requirements'):
    abspath = os.path.abspath(dirpath)
    types   = [os.path.splitext(fname)[0] for fname in os.listdir(abspath)]

    if not os.path.exists(abspath):
        raise ValueError('Directory {directory} not found.'.format(directory = abspath))
    elif not os.path.isdir(abspath):
        raise ValueError('{directory} is not a directory.'.format(directory = abspath))

    if type_:
        if type_ in types:
            with open(os.path.join(abspath, '{type_}.txt'.format(type_ = type_)), mode = 'r') as f:
                dependencies = [line.strip() for line in f if line]
                
                return dependencies
        else:
            raise ValueError('Incorrect dependency type {type_}'.format(type_ = type_))
    else:
        dependencies = dict()
        
        for type_ in types:
            dependencies[type_] = get_dependencies(type_)
        
        return dependencies

package = dict(
    name             = 'schema',
    version          = __version__,
    # TODO: description
    description      = '',
    long_description = get_long_description('README.md', 'LICENSE'),
    homepage         = 'https://github.com/achillesrasquinha/schema',
    authors          = \
    [
        { 'name': 'Achilles Rasquinha', 'email': 'achillesrasquinha@gmail.com' }
    ],
    license          = 'MIT',
    classifiers      = \
    [

    ],
    keywords         = \
    [
        'schema',
        'metadata',
        'semantic'
    ],
    dependencies     = get_dependencies()
)