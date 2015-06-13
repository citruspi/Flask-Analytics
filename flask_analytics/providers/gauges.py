from flask_analytics.providers.base import BaseProvider


class Gauges(BaseProvider):

    site_id = None

    def __init__(self, site_id=None):
        self.site_id = site_id

    @property
    def template(self):
        return """<script type="text/javascript">
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

    @property
    def source(self):
        if self.site_id is None:
            return None
        return self.template.format(site_id=self.site_id)
