install:

	python setup.py install

develop:

	python setup.py develop

test: develop

	nosetests -v --with-coverage --cover-package=flask_analytics --cover-html

.PHONY: install develop
