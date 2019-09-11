import re


def scan_source(source):
    regex = re.compile('wp-content/[mu-]*plugins/([^/]+)/.+ver=([0-9\.]+)')
    return list(set(regex.findall(source)))