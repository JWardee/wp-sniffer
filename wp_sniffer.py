import os

from scan_manager import ScanManager

url = input("URL to scan [%s]: " % os.getenv("DEFAULT_URL")) or os.getenv("DEFAULT_URL")

print(ScanManager().run_all(url))
