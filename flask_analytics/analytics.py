from flask import Flask, Markup
from pprint import pprint
from flask_analytics.providers.gosquared import GoSquared
class Generate(object):

    @staticmethod
    def chartbeat(uid, domain):

        template = """<script type="text/javascript">
    var _sf_async_config={{}};
    /** CONFIGURATION START **/
    _sf_async_config.uid = {uid}; /** CHANGE THIS **/
    _sf_async_config.domain = "{domain}"; /** CHANGE THIS **/
    /** CONFIGURATION END **/
    (function(){{
        function loadChartbeat() {{
            window._sf_endpt=(new Date()).getTime();
            var e = document.createElement("script");
            e.setAttribute("language", "javascript");
            e.setAttribute("type", "text/javascript");
            e.setAttribute('src', '//static.chartbeat.com/js/chartbeat.js');
            document.body.appendChild(e);
        }}
        var oldonload = window.onload;
        window.onload = (typeof window.onload != "function") ?
        loadChartbeat : function() {{ oldonload(); loadChartbeat(); }};
    }})();
</script>"""

        return template.format(uid=uid, domain=domain)

    @staticmethod
    def piwik(base_url, site_id):

        template = """<script type="text/javascript">
    var _paq = _paq || [];
    (function(){{
        var u=(("https:" == document.location.protocol) ? "https://{base_url}/" : "http://{base_url}/");
        _paq.push(['setSiteId', {site_id}]);
        _paq.push(['setTrackerUrl', u+'piwik.php']);
        _paq.push(['trackPageView']);
        _paq.push(['enableLinkTracking']);
        var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; g.type='text/javascript'; g.defer=true; g.async=true; g.src=u+'piwik.js';
        s.parentNode.insertBefore(g,s);
    }})();
</script>"""

        return template.format(base_url=base_url, site_id=site_id)

    @staticmethod
    def gauges(site_id):

        template = """<script type="text/javascript">
    var _gauges = _gauges || [];
    (function() {{
        var t   = document.createElement('script');
        t.type  = 'text/javascript';
        t.async = true;
        t.id    = 'gauges-tracker';
        t.setAttribute('data-site-id', '{site_id}');
        t.src = '//secure.gaug.es/track.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(t, s);
    }})();
</script>"""

        return template.format(site_id = site_id)

    @staticmethod
    def google_analytics(account):

        template = """<script type="text/javascript">

    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', '{account}']);
    _gaq.push(['_trackPageview']);

    (function() {{
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    }})();

</script>"""

        return template.format(account=account)

class Analytics(object):

    def __init__ (self, app=None, disable_context_processor=False):

        self.app = app
        self.snippets = {}

        if app is not None:

            self.init_app(app, not(disable_context_processor))

    def init_app(self, app, context_processor):

        if 'GOOGLE_ANALYTICS_ID' in app.config:

            self.snippets['google'] = Generate.google_analytics(
                                        app.config['GOOGLE_ANALYTICS_ID'])

        if 'GAUGES_SITEID' in app.config:

            self.snippets['gauges'] = Generate.gauges(
                                        app.config['GAUGES_SITEID'])

        if (('PIWIK_BASEURL' in app.config) and
            ('PIWIK_SITEID' in app.config)):

            self.snippets['piwik'] = Generate.piwik(
                                        app.config['PIWIK_BASEURL'],
                                        app.config['PIWIK_SITEID'])

        if (('CHARTBEAT_UID' in app.config) and
            ('CHARTBEAT_DOMAIN' in app.config)):

            self.snippets['chartbeat'] = Generate.chartbeat(
                                            app.config['CHARTBEAT_UID'],
                                            app.config['CHARTBEAT_DOMAIN'])

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
