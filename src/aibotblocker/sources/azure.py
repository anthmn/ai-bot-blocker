"""
Azure IP address fetcher.
"""

import json
import re
import urllib.request
from aibotblocker.utils.ipv4 import is_ipv4


def parse_ips(
    data,  # type: dict
):
    """
    Parse IPs from Azure data.

    :param data: Azure IP data.
    :type data: dict
    :return: IPs
    :rtype: list[str]
    """
    ips = []

    for block in data["values"]:
        ips += block["properties"]["addressPrefixes"]

    ips = list(filter(is_ipv4, ips))
    ips = list(sorted(ips))

    return ips


def fetch_ips():
    """
    Fetch IP addresses.

    :return: IP addresses.
    :rtype: List[str]
    """
    url = "https://www.microsoft.com/en-us/download/details.aspx?id=56519"

    with urllib.request.urlopen(url) as response:
        data = response.read().decode()

    url_regex = re.compile("https://download.microsoft.com/.*?.json")
    url = re.search(url_regex, data).group()

    with urllib.request.urlopen(url) as response:
        data = response.read().decode()

    data = json.loads(data)
    ips = parse_ips(data)
    ips = list(sorted(ips))

    return ips
