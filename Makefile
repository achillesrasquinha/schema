BASEDIR   = $(realpath .)
PACKAGE   = schema
SOURCEDIR = $(realpath $(PACKAGE))

clean:
	python setup.py clean

	clear

install:
	cat requirements/*.txt          > requirements-dev.txt
	cat requirements/production.txt > requirements.txt

	pip install -r requirements-dev.txt

	python setup.py install

	make clean

test:
	make install

	python setup.py test

all:
	make install test clean