"""
AWS IP address fetcher.
"""

import json
import urllib.request


def fetch_ips():
    """
    Fetch IP addresses.

    :return: IP addresses.
    :rtype: List[str]
    """
    url = "https://ip-ranges.amazonaws.com/ip-ranges.json"

    with urllib.request.urlopen(url) as response:
        data = response.read().decode()

    ips = json.loads(data)
    ips = ips["prefixes"]
    ips = list(map(lambda ip: ip["ip_prefix"], ips))
    ips = list(sorted(ips))

    return ips
