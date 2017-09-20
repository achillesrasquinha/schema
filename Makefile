.PHONY: build

PYTHON   ?= python

BASEDIR   = $(realpath .)
PACKAGE   = schema
SOURCEDIR = $(realpath $(PACKAGE))

MODELSDIR = $(realpath models)

clean:
	python setup.py clean

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

build:
	rm -rf models/*
	
	$(PYTHON) -B -m bot --dest $(MODELSDIR)

all:
	make install test clean