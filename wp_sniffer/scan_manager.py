import os

import wp_sniffer.db_manager as db_manager
import wp_sniffer.utilities as utilities
from wp_sniffer.scans.assets_in_source import AssetsInSource
from wp_sniffer.scans.meta_tags import MetaTags
from wp_sniffer.scans.rss_feed import RssFeed


class ScanManager:
    def run_all(self, url, _formatter=os.getenv("OUTPUT_FORMATTER")):
        db_manager.update_db()
        assets_in_source = AssetsInSource(url, None)

        results = RssFeed(url, None).results
        results += assets_in_source.results
        results += MetaTags(url, assets_in_source.html_source).results

        formatter = utilities.import_file("wp_sniffer.output_formatters." + _formatter, ['format_output'])

        return formatter.format_output(self.remove_duplicate_results_by_confidence(results))

    def remove_duplicate_results_by_confidence(self, results):
        processed_results = list()

        for result in results:
            if any(process_result.get('slug', None) == result['slug'] for process_result in processed_results):
                for index, process_result in enumerate(processed_results):
                    if result['slug'] == process_result['slug'] and result['confidence'] > process_result['confidence']:
                        processed_results[index] = result
                        break
            else:
                processed_results.append(result)

        return processed_results
