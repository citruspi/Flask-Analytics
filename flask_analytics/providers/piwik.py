from flask_analytics.providers.base import BaseProvider


class Piwik(BaseProvider):

    base_url = None
    site_id = None

    def __init__(self, base_url=None, site_id=None):
        self.base_url = base_url
        self.site_id = site_id

    @property
    def template(self):
        return """<script type="text/javascript">
    var _paq = _paq || [];
    (function(){{
        var u=(("https:" == document.location.protocol) ? "https://{base_url}/" : "http://{base_url}/");
        _paq.push(['setSiteId', '{site_id}']);
        _paq.push(['setTrackerUrl', u+'piwik.php']);
        _paq.push(['trackPageView']);
        _paq.push(['enableLinkTracking']);
        var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; g.type='text/javascript'; g.defer=true; g.async=true; g.src=u+'piwik.js';
        s.parentNode.insertBefore(g,s);
    }})();
</script>"""

    @property
    def source(self):
        if self.base_url is None or self.site_id is None:
            return None
        return self.template.format(base_url=self.base_url,
                                    site_id=self.site_id)
