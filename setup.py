import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

package_name = "wp_sniffer"
package_username = "jwardee"
package_fullname = package_name + "_" + package_username

setuptools.setup(
    name= package_fullname,
    version="0.0.1",
    author="James Ward",
    author_email="python@jamesward.io",
    scripts=[package_name + '/' + package_name],
    install_requires=['requests',
                      'beautifulsoup4',
                      'stringcase',
                      'python-dotenv',
                      'dicttoxml'],
    description="Detect information about a WordPress site including what plugins and themes along with their versions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JWardee/wp-sniffer",
    package_data={package_name: ['db/.gitkeep', '.env']},
    packages=[package_name, package_name + '/scans', package_name + '/output_formatters'],#setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
