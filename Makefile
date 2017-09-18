BASEDIR   = $(realpath .)
PACKAGE   = schema
SOURCEDIR = $(realpath $(PACKAGE))

install:
	cat requirements/*.txt 			> requirements-dev.txt
	cat requirements/production.txt > requirements.txt

	pip install -r requirements-dev.txt

clean:
	find $(BASEDIR) | grep -E "__pycache__|.pyc" | xargs rm -rf

	clear

test:
	pytest $(SOURCEDIR)

all:
	make install test clean