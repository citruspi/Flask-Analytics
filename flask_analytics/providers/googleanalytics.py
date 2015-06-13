from flask_analytics.providers.base import BaseProvider


class GoogleAnalytics(BaseProvider):

    account = None
    enabled = True

    def __init__(self, account=None, enabled=True):
        self.account = account
        self.enabled = enabled

    @property
    def template(self):
        return """<script type="text/javascript">

    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', '{account}']);
    _gaq.push(['_trackPageview']);

    (function() {{
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    }})();

</script>"""

    def __str__(self):
        if self.enabled:
            return self.template.format(account=self.account)
        else:
            return ''
