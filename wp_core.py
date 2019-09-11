import re
import requests


def get_version_from_rss(url):
    source = requests.get(url + "/feed").text
    regex = re.compile('wordpress\.org/\?v=([0-9\.]+)')
    results = regex.findall(source)
    return results[0] if results else False
