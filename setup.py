import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wp-sniffer-pkg-jwardee",
    version="0.0.1",
    author="James Ward",
    author_email="python@jamesward.io",
    description="Detect information about a WordPress site including what plugins and themes along with their versions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JWardee/wp-sniffer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)