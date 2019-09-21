import re
from scans.scan import Scan


class RssFeed(Scan):
    def __init__(self, page_url, _html_source=None):
        super().__init__( page_url + "/feed", _html_source)
        self.discovery_method = "rss-feed"
        self.confidence = 70

    def scan(self):
        regex = re.compile('wordpress\.org/\?v=([0-9\.]+)')
        results = regex.findall(self.html_source)
        return results[0] if results else False

    def parse_results(self, result):
        return [self.get_result_object("wordpress", result, "core")]
