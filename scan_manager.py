from scans.assets_in_source import AssetsInSource
from scans.meta_tags import MetaTags
from scans.rss_feed import RssFeed


class ScanManager:
    def run_all(self, url):
        # TODO: Remove duplicate results based on their confidence,
        # lower ones are removed in favour of higher ones

        assets_in_source = AssetsInSource(url)
        return RssFeed(url).results + \
               assets_in_source.results + \
               MetaTags(url, assets_in_source.html_source).results
