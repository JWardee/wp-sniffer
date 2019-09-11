import db_manager
import requests
import wp_core
import wp_plugins

defaultUrl = "https://homeandroost.co.uk"
url = input("URL to scan [%s]: " % defaultUrl) or defaultUrl

print("Scanning %s..." % url)
print("Checking if plugin CSV file exists...")

if not db_manager.csv_list_exists():
    print("Creating CSV file...")
    db_manager.create_csv_list_of_all_plugins()

wp_core_version = wp_core.get_version_from_rss(url)

print("WordPress version is %s" % wp_core_version if wp_core_version else "WordPress version not found")

source = requests.get(url).text

for result in wp_plugins.scan_source(source):
    print("Found %s running version %s" % (result[0], result[1]))
