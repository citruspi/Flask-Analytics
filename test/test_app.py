import unittest
import re
from app import app, analytics

class TestAnalytics(unittest.TestCase):

    def test_boostrap(self):

        expected = {
            'CHARTBEAT': {
                'DOMAIN': None,
                'ENABLED': True,
                'UID': None
            },
            'ENABLED': True,
            'GAUGES': {
                'ENABLED': True,
                'SITE_ID': None
            },
            'GOOGLE_CLASSIC_ANALYTICS': {
                'ACCOUNT': None,
                'ENABLED': True
            },
            'GOOGLE_UNIVERSAL_ANALYTICS': {
                'ACCOUNT': None,
                'ENABLED': True
            },
            'GOSQUARED': {
                'ENABLED': True,
                'UID': None
            },
            'PIWIK': {
                'BASE_URL': None,
                'ENABLED': True,
                'SITE_ID': None
            }
        }

        self.assertEquals(analytics.bootstrap, expected)

    def test_none(self):

        self.test_app = app.test_client()

        response = self.test_app.get('/none/')

        expected = ""

        self.assertEquals(response.data, expected.encode('utf8'))

    def test_disabled(self):

        self.test_app = app.test_client()

        response = self.test_app.get('/disabled/')

        expected = ""

        self.assertEquals(response.data, expected.encode('utf8'))


    def test_chartbeat(self):

        self.test_app = app.test_client()

        response = self.test_app.get('/chartbeat/')

        expected = """<script type="text/javascript">
    var _sf_async_config={};
    /** CONFIGURATION START **/
    _sf_async_config.uid = "uiP3eeKie6ohDo6"; /** CHANGE THIS **/
    _sf_async_config.domain = "eeda8Otheefu5qu"; /** CHANGE THIS **/
    /** CONFIGURATION END **/
    (function(){
        function loadChartbeat() {
            window._sf_endpt=(new Date()).getTime();
            var e = document.createElement("script");
            e.setAttribute("language", "javascript");
            e.setAttribute("type", "text/javascript");
            e.setAttribute('src', '//static.chartbeat.com/js/chartbeat.js');
            document.body.appendChild(e);
        }
        var oldonload = window.onload;
        window.onload = (typeof window.onload != "function") ?
        loadChartbeat : function() { oldonload(); loadChartbeat(); };
    })();
</script>"""

        self.assertEquals(response.data, expected.encode('utf8'))

    def test_gosquared(self):

        self.test_app = app.test_client()

        response = self.test_app.get('/gosquared/')

        expected = """<script>
    !function(g,s,q,r,d){r=g[r]=g[r]||function(){(r.q=r.q||[]).push(
    arguments)};d=s.createElement(q);q=s.getElementsByTagName(q)[0];
    d.src='//d1l6p2sc9645hc.cloudfront.net/tracker.js';q.parentNode.
    insertBefore(d,q)}(window,document,'script','_gs');

    _gs('ahz1Nahqueorahw');
</script>"""

        self.assertEquals(response.data, expected.encode('utf8'))

    def test_piwik(self):

        self.test_app = app.test_client()

        response = self.test_app.get('/piwik/')

        expected = """<script type="text/javascript">
    var _paq = _paq || [];
    (function(){
        var u=(("https:" == document.location.protocol) ? "https://aeniki8pheiFiad/" : "http://aeniki8pheiFiad/");
        _paq.push(['setSiteId', 'uiP3eeKie6ohDo6']);
        _paq.push(['setTrackerUrl', u+'piwik.php']);
        _paq.push(['trackPageView']);
        _paq.push(['enableLinkTracking']);
        var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; g.type='text/javascript'; g.defer=true; g.async=true; g.src=u+'piwik.js';
        s.parentNode.insertBefore(g,s);
    })();
</script>"""

        self.assertEquals(response.data, expected.encode('utf8'))

    def test_gauges(self):

        self.test_app = app.test_client()

        response = self.test_app.get('/gauges/')

        expected = """<script type="text/javascript">
    var _gauges = _gauges || [];
    (function() {
        var t   = document.createElement('script');
        t.type  = 'text/javascript';
        t.async = true;
        t.id    = 'gauges-tracker';
        t.setAttribute('data-site-id', 'soV5eile3aiFi9E');
        t.src = '//secure.gaug.es/track.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(t, s);
    })();
</script>"""

        self.assertEquals(response.data, expected.encode('utf8'))

    def test_google_classic(self):

        self.test_app = app.test_client()

        response = self.test_app.get('/google-classic/')

        expected = """<script type="text/javascript">

    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'wiengech9tiefuW']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();

</script>"""

        self.assertEquals(response.data, expected.encode('utf8'))

    def test_google_universal(self):

        self.test_app = app.test_client()

        response = self.test_app.get('/google-universal/')

        expected = """<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'iqmbak3kfpdg2N', 'auto');
  ga('send', 'pageview');

</script>"""

        self.assertEquals(response.data, expected.encode('utf8'))


    def test_all(self):

        self.test_app = app.test_client()

        response = self.test_app.get('/')

        expected = """<script>
    !function(g,s,q,r,d){r=g[r]=g[r]||function(){(r.q=r.q||[]).push(
    arguments)};d=s.createElement(q);q=s.getElementsByTagName(q)[0];
    d.src='//d1l6p2sc9645hc.cloudfront.net/tracker.js';q.parentNode.
    insertBefore(d,q)}(window,document,'script','_gs');

    _gs('ahz1Nahqueorahw');
</script>
<script type="text/javascript">
    var _gauges = _gauges || [];
    (function() {
        var t   = document.createElement('script');
        t.type  = 'text/javascript';
        t.async = true;
        t.id    = 'gauges-tracker';
        t.setAttribute('data-site-id', 'soV5eile3aiFi9E');
        t.src = '//secure.gaug.es/track.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(t, s);
    })();
</script>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'iqmbak3kfpdg2N', 'auto');
  ga('send', 'pageview');

</script>
<script type="text/javascript">

    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'wiengech9tiefuW']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();

</script>
<script type="text/javascript">
    var _paq = _paq || [];
    (function(){
        var u=(("https:" == document.location.protocol) ? "https://aeniki8pheiFiad/" : "http://aeniki8pheiFiad/");
        _paq.push(['setSiteId', 'uiP3eeKie6ohDo6']);
        _paq.push(['setTrackerUrl', u+'piwik.php']);
        _paq.push(['trackPageView']);
        _paq.push(['enableLinkTracking']);
        var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; g.type='text/javascript'; g.defer=true; g.async=true; g.src=u+'piwik.js';
        s.parentNode.insertBefore(g,s);
    })();
</script>
<script type="text/javascript">
    var _sf_async_config={};
    /** CONFIGURATION START **/
    _sf_async_config.uid = "uiP3eeKie6ohDo6"; /** CHANGE THIS **/
    _sf_async_config.domain = "eeda8Otheefu5qu"; /** CHANGE THIS **/
    /** CONFIGURATION END **/
    (function(){
        function loadChartbeat() {
            window._sf_endpt=(new Date()).getTime();
            var e = document.createElement("script");
            e.setAttribute("language", "javascript");
            e.setAttribute("type", "text/javascript");
            e.setAttribute('src', '//static.chartbeat.com/js/chartbeat.js');
            document.body.appendChild(e);
        }
        var oldonload = window.onload;
        window.onload = (typeof window.onload != "function") ?
        loadChartbeat : function() { oldonload(); loadChartbeat(); };
    })();
</script>"""



        response_sections = sorted(re.split('<|>',str(response.data)))
        expected_sections = sorted(re.split('<|>',str(expected.encode('utf'))))

        self.assertEquals(response_sections, expected_sections)
