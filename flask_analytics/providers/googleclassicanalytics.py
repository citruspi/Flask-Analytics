from flask_analytics.providers.base import BaseProvider


class GoogleClassicAnalytics(BaseProvider):

    account = None

    def __init__(self, account=None):
        self.account = account

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

    @property
    def source(self):
        if self.account is None:
            return None
        return self.template.format(account=self.account)
