[![Travis branch](https://img.shields.io/travis/citruspi/Flask-Analytics/master.svg?style=flat-square)]()
[![Coveralls branch](https://img.shields.io/coveralls/citruspi/Flask-Analytics/master.svg?style=flat-square)]()
[![License](https://img.shields.io/github/license/citruspi/Flask-Analytics.svg?style=flat-square)]()
[![PyPI](https://img.shields.io/pypi/dm/Flask-Analytics.svg?style=flat-square)]()
[![PyPI](https://img.shields.io/pypi/v/Flask-Analytics.svg?style=flat-square)]()
[![PyPI](https://img.shields.io/pypi/wheel/Flask-Analytics.svg?style=flat-square)]()
[![PyPI](https://img.shields.io/pypi/pyversions/Flask-Analytics.svg?style=flat-square)]()
[![PyPI](https://img.shields.io/pypi/status/Flask-Analytics.svg?style=flat-square)]()

## Flask-Analytics

Flask Analytics is an extension for Flask which generates analytics snippets for inclusion in templates.

## Installation

```bash
$ pip install Flask-Analytics
```

## Usage

__app.py__

```python
from flask import Flask, render_template
from flask_analytics import Analytics

app = Flask(__name__)
Analytics(app)

app.config['ANALYTICS']['GAUGES']['SITE_ID'] = 'XXXXXXXXXXXXX'


@app.route('/')
def index():

    return render_template('index.html')
```

__index.html__

```
{{ analytics }}
```

__result__

```html
$ curl http://localhost:5000/
<script type="text/javascript">
    var _gauges = _gauges || [];
    (function() {
        var t   = document.createElement('script');
        t.type  = 'text/javascript';
        t.async = true;
        t.id    = 'gauges-tracker';
        t.setAttribute('data-site-id', 'XXXXXXXXXXXXX');
        t.src = '//secure.gaug.es/track.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(t, s);
    })();
</script>
```

## Services

`Flask-Analytics` uses keys defined in `app.config['ANALYTICS']` to determine which for which services analytics snippets should be generated.

| Service | Keys Required |
|:--------|:--------------|
| [Google Analytics (ga.js)](http://www.google.com/analytics/) | `['GOOGLE_CLASSIC_ANALYTICS']['ACCOUNT']` |
| [Universal Analytics (analytics.js) ](http://www.google.com/analytics/) | `['GOOGLE_UNIVERSAL_ANALYTICS']['ACCOUNT']` |
| [Piwik](http://piwik.org/) | `['PIWIK']['BASE_URL']`<br>`['PIWIK']['SITE_ID']`|
| [Gaug.es](http://gaug.es/) | `['GAUGES']['SITE_ID']` |
| [Chartbeat](https://chartbeat.com) | `['CHARTBEAT']['UID']`<br>`['CHARTBEAT']['DOMAIN']` |
| [GoSquared](https://www.gosquared.com) | `['GOSQUARED']['UID']` |

Individual services can be disabled by setting the `ENABLED` key for that service (e.g. `['ANALYTICS']['PIWIK']['ENABLED']`). Analytics as a whole can be disabled by setting the `ENABLED` key at the top (e.g. `['ANALYTICS']['ENABLED']`).

When a service, or analytics as a whole, is disabled, it returns an empty string, so it's safe to keep `{{analytics}}` in your template.

When the configuration changes, the source for the analytics code will automatically be rebuilt the next time it's called.

## Tests

```
$ nosetests -v --with-coverage --cover-package=flask_analytics --cover-html 
test_all (test_app.TestAnalytics) ... ok
test_boostrap (test_app.TestAnalytics) ... ok
test_chartbeat (test_app.TestAnalytics) ... ok
test_disabled (test_app.TestAnalytics) ... ok
test_gauges (test_app.TestAnalytics) ... ok
test_google_classic (test_app.TestAnalytics) ... ok
test_google_universal (test_app.TestAnalytics) ... ok
test_gosquared (test_app.TestAnalytics) ... ok
test_none (test_app.TestAnalytics) ... ok
test_piwik (test_app.TestAnalytics) ... ok

Name                                                    Stmts   Miss  Cover   Missing
-------------------------------------------------------------------------------------
flask_analytics.py                                          1      0   100%   
flask_analytics/analytics.py                               60      1    98%   77
flask_analytics/providers.py                                0      0   100%   
flask_analytics/providers/base.py                           2      0   100%   
flask_analytics/providers/chartbeat.py                     13      0   100%   
flask_analytics/providers/gauges.py                        11      0   100%   
flask_analytics/providers/googleclassicanalytics.py        11      0   100%   
flask_analytics/providers/googleuniversalanalytics.py      11      0   100%   
flask_analytics/providers/gosquared.py                     11      0   100%   
flask_analytics/providers/piwik.py                         13      0   100%   
-------------------------------------------------------------------------------------
TOTAL                                                     133      1    99%   
----------------------------------------------------------------------
Ran 10 tests in 0.111s


OK
```

## License

Flask-Analytics is dedicated to the public domain. Please read the license for
more information.
