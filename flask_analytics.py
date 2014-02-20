from flask import Flask, Markup

class AnalyticsEngines(object):

    @staticmethod
    def piwik(piwik_url, siteid):

        return """<script type="text/javascript">
            var _paq = _paq || [];
            (function(){ 
                var u=(("https:" == document.location.protocol) ? "https://%s/" : "http://%s/");
                _paq.push(['setSiteId', %s]);
                _paq.push(['setTrackerUrl', u+'piwik.php']);
                _paq.push(['trackPageView']);
                _paq.push(['enableLinkTracking']);
                var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; g.type='text/javascript'; g.defer=true; g.async=true; g.src=u+'piwik.js';
                s.parentNode.insertBefore(g,s); 
            })();
        </script>""" % (piwik_baseurl, piwik_baseurl, piwik_siteid)

    @staticmethod
    def gauges(gauges_siteid):

      return """<script type="text/javascript">
          var _gauges = _gauges || [];
          (function() {
              var t   = document.createElement('script');
              t.type  = 'text/javascript';
              t.async = true;
              t.id    = 'gauges-tracker';
              t.setAttribute('data-site-id', '%s');
              t.src = '//secure.gaug.es/track.js';
              var s = document.getElementsByTagName('script')[0];
              s.parentNode.insertBefore(t, s);
          })();
      </script>""" % (gauges_siteid)

    @staticmethod
    def google_analytics(google_analytics_id):

      return """<script type="text/javascript">

          var _gaq = _gaq || [];
          _gaq.push(['_setAccount', '%s']);
          _gaq.push(['_trackPageview']);

          (function() {
              var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
              ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
          })();

      </script>""" % (google_analytics_id)

class Analytics(object):

    def __init__ (self, app=None):

        self.app = app
        self.tracking_code = []

        if app is not None:

        	  self.init_app(app)

    def init_app(self, app):

        if 'GOOGLE_ANALYTICS_ID' in app.config:

            self.tracking_code.append(AnalyticsEngines.google_analytics(app.config['GOOGLE_ANALYTICS_ID']))

        if 'GAUGES_SITEID' in app.config:

            self.tracking_code.append(AnalyticsEngines.gauges(app.config['GAUGES_SITEID']))

        if (('PIWIK_BASEURL' in app.config) and
            ('PIWIK_SITEID' in app.config)):

            self.tracking_code.append(AnalyticsEngines.piwik(app.config['PIWIK_BASEURL'],
                                                             app.config['PIWIK_SITEID']))


    @property
    def code(self):

        return Markup('\n'.join(self.tracking_code))
