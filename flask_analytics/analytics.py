from flask import Markup
from flask_analytics.providers.gosquared import GoSquared
from flask_analytics.providers.chartbeat import Chartbeat
from flask_analytics.providers.piwik import Piwik
from flask_analytics.providers.gauges import Gauges
from flask_analytics.providers.googleclassicanalytics import GoogleClassicAnalytics
from flask_analytics.providers.googleuniversalanalytics import GoogleUniversalAnalytics


class Analytics(object):

    provider_map = {
        'gosquared': GoSquared,
        'chartbeat': Chartbeat,
        'piwik': Piwik,
        'gauges': Gauges,
        'google_classic_analytics': GoogleClassicAnalytics,
        'google_universal_analytics': GoogleUniversalAnalytics
    }

    _source = ''
    _config = {}

    def __init__(self, app=None, disable_context_processor=False):
        self.app = app

        if app is not None:
            self.init_app(app, not(disable_context_processor))

    def init_app(self, app, context_processor):
        self.build_source(app.config)

        if context_processor:
            app.context_processor(self._context_processor)

    @property
    def bootstrap(self):
        config = {
            'ENABLED': True,
        }

        for provider in self.provider_map:
            subconfig = {
                'ENABLED': True
            }

            args = self.provider_map[provider].__init__.__code__.co_varnames
            args = [arg for arg in args if arg != 'self']

            for arg in args:
                subconfig[arg.upper()] = None

            config[provider.upper()] = subconfig

        return config

    def build_source(self, config):
        self._source = ''

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

            for key in list(args):
                args[key.lower()] = args.pop(key)

            instance = self.provider_map[provider](**args)

            if instance.source is not None:
                self._source += '\n'
                self._source += Markup(instance.source)

        self._source = self._source.lstrip()
        self._config = config

    @property
    def source(self):
        if self._config != self.app.config:
            self.build_source(self.app.config)

        return self._source

    def _context_processor(self):
        return dict(analytics=self.source)
