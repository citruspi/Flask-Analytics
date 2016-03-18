from flask_analytics.providers.base import BaseProvider


class GoogleUniversalAnalytics(BaseProvider):

    account = None

    def __init__(self, account=None):
        self.account = account

    @property
    def template(self):
        return """<script>
  (function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
  (i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  }})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', '{account}', 'auto');
  ga('send', 'pageview');

</script>"""

    @property
    def source(self):
        if self.account is None:
            return None
        return self.template.format(account=self.account)




  