# inspired by npm's package.json
# imports - standard imports
import os

# expose the __version__
with open('schema/__version__.py') as f:
    code = f.read()
    exec(code)

def get_long_description(*files, dirpath = '.'):
    for f in files:
        pass

def get_dependencies(type_, dirpath = 'requirements'):
    abspath = os.path.abspath(dirpath)

    if not os.path.exists(abspath):
        raise ValueError('Directory {directory} not found.'.format(directory = abspath))
    elif not os.path.isdir(abspath):
        raise ValueError('{directory} is not a directory.'.format(directory = abspath))

package = dict(
    name             = 'schema',
    version          = __version__,
    # TODO: description
    description      = '',
    long_description = get_long_description('README.md', 'LICENSE'),
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
    dependencies     = \
    {
        'production': get_dependencies('production')
    }
)