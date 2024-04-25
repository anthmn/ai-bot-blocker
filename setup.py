#!/bin/python3


"""
Ichido AI And LLM Bot Blocker.
"""

from src.aibotblocker.version import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "name": "aibotblocker",
    "version": __version__,
    "url": "https://git.ichi.do/anthony/ai-bot-blocker",
    "download_url": "https://files.ichi.do/",
    "project_urls": {},
    "description": "Ichido AI And LLM Bot Blocker.",
    "long_description": open("README.md", "r", encoding="utf-8").read(),
    "long_description_content_type": "text/x-markdown",
    "author": "Anthony Mancini",
    "author_email": "anthony.m.mancini@protonmail.com",
    "maintainer": "Anthony Mancini",
    "maintainer_email": "anthony.m.mancini@protonmail.com",
    "license": "AGPL-3.0",
    "packages": [
        "aibotblocker",
        "aibotblocker.firewalls",
        "aibotblocker.servers",
        "aibotblocker.sources",
        "aibotblocker.standards",
        "aibotblocker.tests",
        "aibotblocker.utils",
    ],
    "package_dir": {"": "src"},
    "include_package_data": True,
    "scripts": ["bin/aibotconf"],
    "install_requires": [],
    "classifiers": [
        "Development Status :: Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
}

if __name__ == "__main__":
    setup(**config)
