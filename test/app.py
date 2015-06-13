from flask import Flask, render_template
from flask_analytics import Analytics

app = Flask(__name__)

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

Analytics(app)

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/google/')
def google():

    return render_template('google.html')


@app.route('/gauges/')
def gauges():

    return render_template('gauges.html')


@app.route('/piwik/')
def piwik():

    return render_template('piwik.html')


@app.route('/gosquared/')
def gosquared():

    return render_template('gosquared.html')


@app.route('/chartbeat/')
def chartbeat():

    return render_template('chartbeat.html')

if __name__ == '__main__':

    app.run()
