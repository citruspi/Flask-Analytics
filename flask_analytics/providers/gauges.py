from flask_analytics.providers.base import BaseProvider


class Gauges(BaseProvider):

    site_id = None
    enabled = True

    def __init__(self, site_id=None, enabled=True):
        self.site_id = site_id
        self.enabled = enabled

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

    def __str__(self):
        if self.enabled:
            return self.template.format(site_id=self.site_id)
        else:
            return ''
