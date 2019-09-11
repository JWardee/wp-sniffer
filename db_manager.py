from bs4 import BeautifulSoup
import os.path
import requests

wpPluginsSvnRepoUrl = "https://plugins.svn.wordpress.org"
csvListFileName = "./db/all-plugin-slugs.csv"


def csv_list_exists():
    return os.path.exists(csvListFileName)


def create_csv_list_of_all_plugins():
    soup = BeautifulSoup(requests.get(wpPluginsSvnRepoUrl).text, 'html.parser')
    plugin_slugs = ["Slug"]

    for link in soup.find_all("a"):
        plugin_slugs.append(link.string.replace("/", ""))

    all_plugins_file = open(csvListFileName, "w")
    all_plugins_file.write("\n".join(plugin_slugs))
    all_plugins_file.close()

