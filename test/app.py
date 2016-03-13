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
        },
        'UNIVERSAL_ANALYTICS':{
            'ACCOUNT': 'iqmbak3kfpdg2N'
        }
    }

    return render_template('index.html')


@app.route('/disabled/')
def disabled():

    app.config['ANALYTICS'] = {
        'ENABLED': False,
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
        },
        'UNIVERSAL_ANALYTICS':{
            'ACCOUNT': 'iqmbak3kfpdg2N'
        }
    }

    return render_template('index.html')


@app.route('/none/')
def none():

    if 'ANALYTICS' in app.config:
        del app.config['ANALYTICS']

    return render_template('index.html')


@app.route('/google/')
def google():

    app.config['ANALYTICS'] = {
        'GOOGLE_ANALYTICS': {
            'ACCOUNT': 'wiengech9tiefuW',
        }
    }

    return render_template('index.html')


@app.route('/gauges/')
def gauges():

    app.config['ANALYTICS'] = {
        'GAUGES': {
            'SITE_ID': 'soV5eile3aiFi9E'
        }
    }

    return render_template('index.html')


@app.route('/piwik/')
def piwik():

    app.config['ANALYTICS'] = {
        'PIWIK': {
            'BASE_URL': 'aeniki8pheiFiad',
            'SITE_ID': 'uiP3eeKie6ohDo6',
        }
    }

    return render_template('index.html')


@app.route('/gosquared/')
def gosquared():

    app.config['ANALYTICS'] = {
        'GOSQUARED': {
            'UID': 'ahz1Nahqueorahw'
        }
    }

    return render_template('index.html')


@app.route('/chartbeat/')
def chartbeat():

    app.config['ANALYTICS'] = {
        'CHARTBEAT': {
            'UID': 'uiP3eeKie6ohDo6',
            'DOMAIN': 'eeda8Otheefu5qu'
        }
    }

    return render_template('index.html')

@app.route('/universal/')
def universal():

    app.config['ANALYTICS'] = {
        'UNIVERSAL_ANALYTICS': {
            'ACCOUNT': 'iqmbak3kfpdg2N',
        }
    }

    return render_template('index.html')

if __name__ == '__main__':

    app.run()
