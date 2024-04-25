"""
IIS config builder.
"""


def create_user_agent_line(
    user_agent,  # type: str
):
    """
    Create a User-Agent block line.

    :param user_agent: User-Agent.
    :type user_agent: str
    :return: Config.
    :rtype: str
    """
    line = (
        '      <filteringRule name="Block '
        + user_agent
        + '" scanUrl="false" scanQueryString="false">'
    )
    line += "<scanHeaders>"
    line += '<add requestHeader="User-Agent" />'
    line += "</scanHeaders>"
    line += "<denyStrings>"
    line += '<add string="' + user_agent + '" />'
    line += "</denyStrings>"
    line += "</filteringRule>"
    line += "\n"

    return line


def create_config(
    comment,  # type: str
    user_agents,  # type: list[str]
):
    """
    Create config to block User-Agents.

    :param comment: Comment header.
    :type comment: str
    :param user_agents: User-Agents.
    :type user_agents: list[str]
    :return: Config.
    :rtype: str
    """
    conf = ""
    conf += "<!-- " + comment + " -->\n"
    conf += "<security>\n"
    conf += "  <requestFiltering>\n"
    conf += "    <filteringRules>\n"

    for user_agent in user_agents:
        conf += create_user_agent_line(user_agent)

    conf += "    </filteringRules>\n"
    conf += "  </requestFiltering>\n"
    conf += "</security>\n"

    conf = conf.strip()

    return conf
