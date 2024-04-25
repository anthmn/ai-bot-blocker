import re

IPV4_PATTERN = "^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\\.(?!$)|$)){4}$"
IPV4_RE = re.compile(IPV4_PATTERN)


def is_ipv4(
    ip,  # type: str
):
    """
    Predicate to check if an IP is an IPv4

    :param ip: IP address.
    :type ip: str
    :return: Boolean.
    :rtype: bool
    """

    return IPV4_RE.search(ip.split("/")[0]) is not None
