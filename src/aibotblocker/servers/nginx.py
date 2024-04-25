"""
Nginx config builder.
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
    return 'if ($http_user_agent ~* "' + user_agent + '") { return 403; }\n'


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
    conf += "#\n"
    conf += "# " + comment + "\n"
    conf += "#\n"

    for user_agent in user_agents:
        conf += create_user_agent_line(user_agent)

    return conf
