.PHONY: build
.PHONY: docs

PYTHON   ?= python

BASEDIR   = $(realpath .)
PACKAGE   = schema
SOURCEDIR = $(realpath $(PACKAGE))
DOCSDIR   = $(BASEDIR)/docs

clean-py:
	python setup.py clean

clean:
	make clean-py

	clear

install:
	cat requirements/*.txt          > requirements-dev.txt
	cat requirements/production.txt > requirements.txt

	pip install -r requirements-dev.txt

	$(PYTHON) setup.py install

	make clean

test:
	make install

	py.test --cov=$(SOURCEDIR)

	python setup.py clean

docs:
	sphinx-build -b html $(DOCSDIR)/source $(DOCSDIR)/build

	make clean-py

all:
	make install test clean