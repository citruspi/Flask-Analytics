from flask import Markup
from flask_analytics.providers.gosquared import GoSquared
from flask_analytics.providers.chartbeat import Chartbeat
from flask_analytics.providers.piwik import Piwik
from flask_analytics.providers.gauges import Gauges
from flask_analytics.providers.googleanalytics import GoogleAnalytics


class Analytics(object):

    provider_map = {
        'gosquared': GoSquared,
        'chartbeat': Chartbeat,
        'piwik': Piwik,
        'gauges': Gauges,
        'google_analytics': GoogleAnalytics
    }

    source = ''

    def __init__(self, app=None, disable_context_processor=False):
        self.app = app

        if app is not None:
            self.init_app(app, not(disable_context_processor))

    def init_app(self, app, context_processor):
        self.build_source(app.config)

        if context_processor:
            app.context_processor(self._context_processor)

    def reload(self):
        self.build_source(self.app.config)

    @property
    def bootstrap(self):
        config = {
            'ENABLED': True
        }

        for provider in self.provider_map:
            subconfig = {
                'ENABLED': True
            }

            args = self.provider_map[provider].__init__.func_code.co_varnames
            args = [arg for arg in args if arg != 'self']

            for arg in args:
                subconfig[arg.upper()] = None

            config[provider.upper()] = subconfig

        return config

    def build_source(self, config):
        self.source = ''

        if 'ANALYTICS' not in config:
            self.app.config['ANALYTICS'] = self.bootstrap

        config = config['ANALYTICS']

        enabled = config.get('ENABLED', True)

        if not enabled:
            return

        for provider in self.provider_map:
            if provider.upper() not in config:
                continue

            enabled = config[provider.upper()].get('ENABLED', True)

            if not enabled:
                continue

            args = config[provider.upper()]

            if 'ENABLED' in args:
                del args['ENABLED']

            for key in args:
                args[key.lower()] = args.pop(key)

            instance = self.provider_map[provider](**args)

            if instance.source is not None:
                self.source += '\n'
                self.source += Markup(instance.source)

        self.source = self.source.lstrip()

    @property
    def code(self):
        return self.source

    def _context_processor(self):
        return dict(analytics=self.code)
