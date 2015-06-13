[![Travis branch](https://img.shields.io/travis/citruspi/Flask-Analytics/master.svg?style=flat-square)]()
[![Coveralls branch](https://img.shields.io/coveralls/citruspi/Flask-Analytics/master.svg?style=flat-square)]()
[![PyPI](https://img.shields.io/pypi/dm/Flask-Analytics.svg?style=flat-square)]()
[![PyPI](https://img.shields.io/pypi/l/Flask-Analytics.svg?style=flat-square)]()

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
app.config['GAUGES_SITEID'] = 'XXXXXXXXXXXXX'

Analytics(app)

@app.route('/')
def index():

    return render_template('index.html')
```

__index.html__

```
{{ analytics }}
```

## Services

`Flask-Analytics` uses keys defined in `app.config` to determine which for which services analytics snippets should be generated.

| Service | Keys Required |
|:--------|:--------------|
| [Google Analytics](http://www.google.com/analytics/) | `GOOGLE_ANALYTICS_ID` |
| [Piwik](http://piwik.org/) | `PIWIK_BASEURL`<br>`PIWIK_SITEID`|
| [Gaug.es](http://gaug.es/) | `GAUGES_SITEID` |
| [Chartbeat](https://chartbeat.com) | `CHARTBEAT_UID`<br>`CHARTBEAT_DOMAIN` |
| [GoSquared](https://www.gosquared.com) | `GOSQUARED_ID` |

## Tests

```
$ nosetests -v
test_all (test_app.TestAnalytics) ... ok
test_chartbeat (test_app.TestAnalytics) ... ok
test_gauges (test_app.TestAnalytics) ... ok
test_google (test_app.TestAnalytics) ... ok
test_gosquared (test_app.TestAnalytics) ... ok
test_piwik (test_app.TestAnalytics) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.079s

OK
```

## License

Flask-Analytics is dedicated to the public domain. Please read the license for
more information.
