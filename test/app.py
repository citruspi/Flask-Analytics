from flask import Flask, render_template
from flask.ext.analytics import Analytics

app = Flask(__name__)

app.config['GAUGES_SITEID'] = 'soV5eile3aiFi9E'

Analytics(app)

@app.route('/')
def index():

    return render_template('index.html')

if __name__ == '__main__':

    app.run(debug)
