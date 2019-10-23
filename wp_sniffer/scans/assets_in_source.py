import re
from wp_sniffer.scans.scan import Scan


class AssetsInSource(Scan):
    def __init__(self, page_url, _html_source=None):
        super().__init__(page_url, _html_source)
        self.discovery_method = "asset-in-source"
        self.confidence = 70

    def scan(self):
        regex = re.compile('wp-content/[mu-]*plugins/([^/]+)/.+ver=([0-9\.]+)')
        return {
            "theme": set(),
            "plugin": set(regex.findall(self.html_source))
        }

    def parse_results(self, all_results):
        _results = list()

        for (result_type, results) in all_results.items():
            for result in results:
                _results.append(self.get_result_object(result[0], result[1], result_type))

        return _results
