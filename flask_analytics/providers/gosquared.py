from flask_analytics.providers.base import BaseProvider


class GoSquared(BaseProvider):

    uid = None

    def __init__(self, uid=None):
        self.uid = uid

    @property
    def template(self):
        return """<script>
    !function(g,s,q,r,d){{r=g[r]=g[r]||function(){{(r.q=r.q||[]).push(
    arguments)}};d=s.createElement(q);q=s.getElementsByTagName(q)[0];
    d.src='//d1l6p2sc9645hc.cloudfront.net/tracker.js';q.parentNode.
    insertBefore(d,q)}}(window,document,'script','_gs');

    _gs('{uid}');
</script>"""

    @property
    def source(self):
        if self.uid is None:
            return None
        return self.template.format(uid=self.uid)
