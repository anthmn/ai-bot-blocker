"""
GCP IP address fetcher.
"""

import json
import urllib.request


def parse_ips(
    data,  # type: dict
):
    """
    Parse IPs from GCP data.

    :param data: GCP IP data
    :type data: dict
    :return: IP addresses.
    :rtype: list[str]
    """
    ips = []

    for prefix in data["prefixes"]:
        if "ipv4Prefix" in prefix:
            ips.append(prefix["ipv4Prefix"])

    return ips


def fetch_ips():
    """
    Fetch IP addresses.

    :return: IP addresses.
    :rtype: List[str]
    """
    url = "https://www.gstatic.com/ipranges/cloud.json"

    with urllib.request.urlopen(url) as response:
        data = response.read().decode()

    data = json.loads(data)
    ips = parse_ips(data)
    ips = list(sorted(ips))

    return ips
