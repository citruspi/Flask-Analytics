## Flask-Analytics

Flask Analytics is an extension for Flask which generates analytics snippets for inclusion in templates.

## Installation

```bash
$ pip install Flask-Analytics
```

## Usage

### Defining Service Keys

`Flask-Analytics` uses keys defined in `app.config` to determine which for which services analytics snippets should be generated.

| Service | Keys Required |
|:--------|:--------------|
| [Google Analytics](http://www.google.com/analytics/) | `GOOGLE_ANALYTICS_ID` |
| [Piwik](http://piwik.org/) | `PIWIK_BASEURL`<br>`PIWIK_SITEID`|
| [Gaug.es](http://gaug.es/) | `GAUGES_SITEID` |

### Integrating with Flask

__app.py__

```python

from flask.ext.analytics import Analytics

app.config['GAUGES_SITEID'] = 'XXXXXXXXXXXXX'

code = Analytics(app)

@app.route('/')
def index():

    return render_template('index.html', analytics=code.code)
```

__index.html__

```
{{ analytics }}
```

### Smoother Integration

You can use `context processors` for smoother integration with flask.

Add

```python
@app.context_processor
def inject_analytics():

    return dict(analytics=analytics.code)
```

to make `{{ analytics }}` available in every rendered template automatically.

## License

Flask-Analytics is distributed under the MIT license.
