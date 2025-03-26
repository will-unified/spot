from setuptools import setup, find_packages

setup(
    name="spot",
    version="0.0.8",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="LANKS",
    description="A Spotify API wrapper with support for authorization flow",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/will-unified/spot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
