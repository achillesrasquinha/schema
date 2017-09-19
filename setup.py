# imports - standard imports
import sys, os, shutil
from distutils.command.clean import clean as Clean

# imports - third-party imports
from setuptools import setup, find_packages

# imports - module imports
from package    import package

class CleanCommand(Clean):
    def run(self):
        Clean.run(self)

        basedir = os.path.abspath(os.path.dirname(__file__))

        for dirname in ['.cache', 'dist', '{name}.egg-info'.format(name = package['name'])]:
            abspath = os.path.join(basedir, dirname)
            shutil.rmtree(abspath)

        for dirpath, dirnames, filenames in os.walk(basedir):
            for filename in filenames:
                _, extension = os.path.splitext(filename)
                
                if extension in ['.pyc']:
                    abspath = os.path.join(dirpath, filename)
                    os.remove(abspath)
                
            for dirname in dirnames:
                if dirname in ['__pycache__']:
                    abspath = os.path.join(dirpath, dirname)
                    shutil.rmtree(abspath)

def main(args = None):
    code = os.EX_OK

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
        packages         = find_packages(exclude = ['test']),
        install_requires = package['dependencies']['production'],
        cmdclass         = \
        {
            'clean': CleanCommand
        }
    )

    setup(**meta)

if __name__ == '__main__':
    args = sys.argv[1:]
    code = main(args)

    sys.exit(code)