from flask import Flask, render_template
from flask_analytics import Analytics

app = Flask(__name__)

analytics = Analytics(app)


@app.route('/')
def index():

    app.config['ANALYTICS'] = {
        'GAUGES': {
            'SITE_ID': 'soV5eile3aiFi9E'
        },
        'GOOGLE_ANALYTICS': {
            'ACCOUNT': 'wiengech9tiefuW',
        },
        'PIWIK': {
            'BASE_URL': 'aeniki8pheiFiad',
            'SITE_ID': 'uiP3eeKie6ohDo6',
        },
        'GOSQUARED': {
            'UID': 'ahz1Nahqueorahw'
        },
        'CHARTBEAT': {
            'UID': 'uiP3eeKie6ohDo6',
            'DOMAIN': 'eeda8Otheefu5qu'
        }
    }

    analytics.reload()

    return render_template('index.html')


@app.route('/none/')
def none():

    if 'ANALYTICS' in app.config:
        del app.config['ANALYTICS']

    analytics.reload()

    return render_template('index.html')


@app.route('/google/')
def google():

    app.config['ANALYTICS'] = {
        'GOOGLE_ANALYTICS': {
            'ACCOUNT': 'wiengech9tiefuW',
        }
    }

    analytics.reload()

    return render_template('index.html')


@app.route('/gauges/')
def gauges():

    app.config['ANALYTICS'] = {
        'GAUGES': {
            'SITE_ID': 'soV5eile3aiFi9E'
        }
    }

    analytics.reload()

    return render_template('index.html')


@app.route('/piwik/')
def piwik():

    app.config['ANALYTICS'] = {
        'PIWIK': {
            'BASE_URL': 'aeniki8pheiFiad',
            'SITE_ID': 'uiP3eeKie6ohDo6',
        }
    }

    analytics.reload()

    return render_template('index.html')


@app.route('/gosquared/')
def gosquared():

    app.config['ANALYTICS'] = {
        'GOSQUARED': {
            'UID': 'ahz1Nahqueorahw'
        }
    }

    analytics.reload()

    return render_template('index.html')


@app.route('/chartbeat/')
def chartbeat():

    app.config['ANALYTICS'] = {
        'CHARTBEAT': {
            'UID': 'uiP3eeKie6ohDo6',
            'DOMAIN': 'eeda8Otheefu5qu'
        }
    }

    analytics.reload()

    return render_template('index.html')

if __name__ == '__main__':

    app.run()
