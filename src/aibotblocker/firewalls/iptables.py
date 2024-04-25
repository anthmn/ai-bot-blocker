"""
IP tables config builder.
"""


def create_ip_line(
    ip,  # type: str
):
    """
    Create an IP block line.

    :param ip: IP address.
    :type ip: str
    :return: Config.
    :rtype: str
    """
    line = ""
    line += (
        "-A INPUT -s " + ip + " -p tcp -m state --state NEW -m tcp --dport 80 -j DROP\n"
    )
    line += (
        "-A INPUT -s "
        + ip
        + " -p tcp -m state --state NEW -m tcp --dport 443 -j DROP\n"
    )

    return line


def create_config(
    comment,  # type: str
    ips,  # type: list[str]
):
    """
    Create config to block User-Agents.

    :param comment: Comment header.
    :type comment: str
    :param ips: IP addresses.
    :type ips: list[str]
    :return: Config.
    :rtype: str
    """
    conf = ""
    conf += "#\n"
    conf += "# " + comment + "\n"
    conf += "#\n"
    conf += "*filter\n"
    conf += ":INPUT ACCEPT [0:0]\n"
    conf += ":FORWARD ACCEPT [0:0]\n"
    conf += ":OUTPUT ACCEPT [0:0]\n"

    for ip in ips:
        conf += create_ip_line(ip)

    conf += "COMMIT"

    return conf
