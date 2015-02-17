import unittest
from app import app

class TestAnalytics(unittest.TestCase):

    def test_analytics(self):

        self.test_app = app.test_client()

        response = self.test_app.get('/')

        self.assertEquals(response.data, """<script type="text/javascript">
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
</script>""") 

