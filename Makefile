install:
	python setup.py install

develop:
	python setup.py develop

test: develop
	nosetests -v --with-coverage --cover-package=flask_analytics --cover-html

publish: test
	python setup.py sdist bdist_wheel upload

.PHONY: install develop publish
