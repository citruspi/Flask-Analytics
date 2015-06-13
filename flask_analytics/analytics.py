from flask import Flask, Markup
from pprint import pprint
from flask_analytics.providers.gosquared import GoSquared
from flask_analytics.providers.chartbeat import Chartbeat
from flask_analytics.providers.piwik import Piwik
from flask_analytics.providers.gauges import Gauges
from flask_analytics.providers.googleanalytics import GoogleAnalytics

class Analytics(object):

    def __init__ (self, app=None, disable_context_processor=False):

        self.app = app
        self.snippets = {}

        if app is not None:

            self.init_app(app, not(disable_context_processor))

    def init_app(self, app, context_processor):

        if 'GOOGLE_ANALYTICS_ID' in app.config:

            g = GoogleAnalytics(account=app.config['GOOGLE_ANALYTICS_ID'])

            self.snippets['google'] = str(g)

        if 'GAUGES_SITEID' in app.config:

            g = Gauges(site_id=app.config['GAUGES_SITEID'])

            self.snippets['gauges'] = str(g)

        if (('PIWIK_BASEURL' in app.config) and
            ('PIWIK_SITEID' in app.config)):

             p = Piwik(base_url=app.config['PIWIK_BASEURL'],
                       site_id=app.config['PIWIK_SITEID'])

             self.snippets['piwik'] = str(p)

        if (('CHARTBEAT_UID' in app.config) and
            ('CHARTBEAT_DOMAIN' in app.config)):

            c = Chartbeat(uid=app.config['CHARTBEAT_UID'],
                          domain=app.config['CHARTBEAT_DOMAIN'])

            self.snippets['chartbeat'] = str(c)

        if 'GOSQUARED_ID' in app.config:

            g = GoSquared(uid=app.config['GOSQUARED_ID'])

            self.snippets['gosquared'] = str(g)
        if context_processor:
            app.context_processor(self._context_processor)

    @property
    def code(self):

        processed = self.snippets.copy()

        processed['all'] = Markup('\n'.join(processed.values()))

        for service in processed.keys():
            if service != 'all':
                processed[service] = Markup(processed[service])

        return processed

    def _context_processor(self):
        return dict(analytics=self.code)
