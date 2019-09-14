import requests
import stringcase


class Scan:
    def __init__(self, page_url, _html_source=None):
        self.page_url = page_url
        self._html_source = _html_source
        self._results = {}

    @property
    def results(self):
        if len(self._results) == 0:
            self.results = self.scan()

        return self._results

    @results.setter
    def results(self, _result):
        self._results = self.parse_results(_result)

    def parse_results(self, _result) -> list:
        return _result

    @property
    def html_source(self):
        if self._html_source is None:
            self._html_source = requests.get(self.page_url).text

        return self._html_source

    def scan(self):
        raise NotImplementedError("Child scan object must override the 'scan' method")

    def get_result_object(self, slug, version, type):
        return {
            "slug": stringcase.lowercase(slug),
            "version": version,
            "type": type,
        }
