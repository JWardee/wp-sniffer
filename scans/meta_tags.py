import re

import stringcase
from bs4 import BeautifulSoup
from scans.scan import Scan


class MetaTags(Scan):
    def scan(self):
        soup = BeautifulSoup(self.html_source, 'html.parser')
        meta_tags = soup.select("meta[name=generator]")
        return meta_tags if meta_tags else False

    def parse_results(self, meta_tags):
        regex = re.compile('content="([a-zA-Z]*) ([0-9\.]*)"')
        results = list()

        for meta_tag in meta_tags:
            result = regex.findall(str(meta_tag))[0]
            key = "core" if result[0] == "WordPress" else "plugin"
            results.append(self.get_result_object(result[0], result[1], key))

        return results

