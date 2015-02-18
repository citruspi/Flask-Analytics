install:

	python setup.py install

develop:

	python setup.py develop

test: develop

	nosetests

.PHONY: install develop
