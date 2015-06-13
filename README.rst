|Travis branch| |Coveralls branch| |PyPI| |PyPI|

Flask-Analytics
---------------

Flask Analytics is an extension for Flask which generates analytics
snippets for inclusion in templates.

Installation
------------

.. code:: bash

    $ pip install Flask-Analytics

Usage
-----

**app.py**

.. code:: python

    from flask import Flask, render_template
    from flask_analytics import Analytics

    app = Flask(__name__)
    Analytics(app)

    app.config['ANALYTICS']['GAUGES']['SITE_ID'] = 'XXXXXXXXXXXXX'


    @app.route('/')
    def index():

        return render_template('index.html')

**index.html**

::

    {{ analytics }}

Services
--------

``Flask-Analytics`` uses keys defined in ``app.config['ANALYTICS']`` to
determine which for which services analytics snippets should be
generated.

+-----------------------------------------------------------+-----------------------------------------------------------+
| Service                                                   | Keys Required                                             |
+===========================================================+===========================================================+
| `Google Analytics <http://www.google.com/analytics/>`__   | ``['GOOGLE_ANALYTICS']['ACCOUNT']``                       |
+-----------------------------------------------------------+-----------------------------------------------------------+
| `Piwik <http://piwik.org/>`__                             | ``['PIWIK']['BASE_URL']``\ \ ``['PIWIK']['SITE_ID']``     |
+-----------------------------------------------------------+-----------------------------------------------------------+
| `Gaug.es <http://gaug.es/>`__                             | ``['GAUGES']['SITE_ID']``                                 |
+-----------------------------------------------------------+-----------------------------------------------------------+
| `Chartbeat <https://chartbeat.com>`__                     | ``['CHARTBEAT']['UID']``\ \ ``['CHARTBEAT']['DOMAIN']``   |
+-----------------------------------------------------------+-----------------------------------------------------------+
| `GoSquared <https://www.gosquared.com>`__                 | ``['GOSQUARED']['UID']``                                  |
+-----------------------------------------------------------+-----------------------------------------------------------+

Individual services can be disabled by setting the ``ENABLED`` key for
that service (e.g. ``['ANALYTICS']['PIWIK']['ENABLED']``). Analytics as
a whole can be disabled by setting the ``ENABLED`` key at the top (e.g.
``['ANALYTICS']['ENABLED']``).

When a service, or analytics as a whole, is disabled, it returns an
empty string, so it's safe to keep ``{{analytics}}`` in your template.

When the configuration changes, the source for the analytics code will
automatically be rebuilt the next time it's called.

Tests
-----

::

    nosetests -v --with-coverage --cover-package=flask_analytics --cover-html
    test_all (test_app.TestAnalytics) ... ok
    test_boostrap (test_app.TestAnalytics) ... ok
    test_chartbeat (test_app.TestAnalytics) ... ok
    test_disabled (test_app.TestAnalytics) ... ok
    test_gauges (test_app.TestAnalytics) ... ok
    test_google (test_app.TestAnalytics) ... ok
    test_gosquared (test_app.TestAnalytics) ... ok
    test_none (test_app.TestAnalytics) ... ok
    test_piwik (test_app.TestAnalytics) ... ok

    Name                                        Stmts   Miss  Cover   Missing
    -------------------------------------------------------------------------
    flask_analytics                                 1      0   100%   
    flask_analytics.analytics                      59      0   100%   
    flask_analytics.providers                       0      0   100%   
    flask_analytics.providers.base                  2      0   100%   
    flask_analytics.providers.chartbeat            13      0   100%   
    flask_analytics.providers.gauges               11      0   100%   
    flask_analytics.providers.googleanalytics      11      0   100%   
    flask_analytics.providers.gosquared            11      0   100%   
    flask_analytics.providers.piwik                13      0   100%   
    -------------------------------------------------------------------------
    TOTAL                                         121      0   100%   
    ----------------------------------------------------------------------
    Ran 9 tests in 0.108s

    OK

License
-------

Flask-Analytics is dedicated to the public domain. Please read the
license for more information.

.. |Travis branch| image:: https://img.shields.io/travis/citruspi/Flask-Analytics/master.svg?style=flat-square
   :target: 
.. |Coveralls branch| image:: https://img.shields.io/coveralls/citruspi/Flask-Analytics/master.svg?style=flat-square
   :target: 
.. |PyPI| image:: https://img.shields.io/pypi/dm/Flask-Analytics.svg?style=flat-square
   :target: 
.. |PyPI| image:: https://img.shields.io/pypi/l/Flask-Analytics.svg?style=flat-square
   :target:
