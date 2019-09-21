import os

import db_manager
from scan_manager import ScanManager

url = input("URL to scan [%s]: " % os.getenv("DEFAULT_URL")) or os.getenv("DEFAULT_URL")

print("Scanning %s..." % url)
print("Checking if plugin CSV file exists...")

if not db_manager.csv_list_exists():
    print("Creating CSV file...")
    db_manager.create_csv_list_of_all_plugins()


print(ScanManager().run_all(url))
