from bs4 import BeautifulSoup
import os.path
import requests


def csv_list_exists():
    return os.path.exists(os.getenv("CSV_PLUGIN_LIST_DIR"))


def create_csv_list_of_all_plugins():
    soup = BeautifulSoup(requests.get(os.getenv("SVN_PLUGIN_REPO")).text, 'html.parser')
    plugin_slugs = ["Slug"]

    for link in soup.find_all("a"):
        plugin_slugs.append(link.string.replace("/", ""))

    all_plugins_file = open(os.getenv("CSV_PLUGIN_LIST_DIR"), "w")
    all_plugins_file.write("\n".join(plugin_slugs))
    all_plugins_file.close()
