from bs4 import BeautifulSoup
# import requests

# GET LATEST HTML FILE FROM SVN
# allPluginsSource = requests.get("https://plugins.svn.wordpress.org")
# allPluginsSourceFile = open("./db/all-plugins-svn-source.html", "w")
# allPluginsSourceFile.write(allPluginsSource.text)
# allPluginsSourceFile.close()

# CREATE CSV FILE WITH PLUGIN SLUGS FROM LOCAL HTML FILE
html = open("./db/all-plugins-svn-source.html", "r")
soup = BeautifulSoup(html.read(), 'html.parser')

pluginSlugs = ["Slug"]

for link in soup.find_all("a"):
    pluginSlugs.append(link.string.replace("/", ""))

allPluginsFile = open("./db/all-plugin-slugs.csv", "w")
allPluginsFile.write("\n".join(pluginSlugs))
allPluginsFile.close()
