# imports - third-party imports
from setuptools import setup, find_packages

# imports - module imports
from package    import package

def main(args = None):
    meta = dict(
        name             = package['name'],
        version          = package['version'],
        description      = package['description'],
        url              = package['homepage'],
        author           = ', '.join([author['name']  for author in package['authors']]),
        author_email     = ', '.join([author['email'] for author in package['authors']]),
        long_description = package['long_description'],
        license          = package['license'],
        classifiers      = package['classifiers'],
        keywords         = ' '.join([keyword for keyword in package['keywords']]),
        packages         = find_packages(exlclude = ['test']),
        install_requires = package['dependencies']['production']
    )

    setup(**meta)

if __name__ == '__main__':
    try:
        args = sys.argv[1:]
        code = main(args)
    except:
        code = 1
    finally:
        sys.exit(code)