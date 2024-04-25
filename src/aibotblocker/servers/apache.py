"""
Apache config builder.
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
    user_agent = user_agent.replace(" ", "\\ ")
    user_agent = user_agent.replace(".", "\\.")

    return "RewriteCond %{HTTP_USER_AGENT} ^.*" + user_agent + ".*$\n"


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
    conf += "<Directory />\n"
    conf += "    Options FollowSymLinks\n"
    conf += "    AllowOverride None\n"
    conf += "    Satisfy Any\n"
    conf += "    Allow from all\n"
    conf += "    RewriteEngine on\n"

    for user_agent in user_agents:
        conf += "    " + create_user_agent_line(user_agent)
        conf += "    RewriteRule . - [R=403,L]\n"

    conf += "</Directory>"

    return conf


def create_htaccess_config(
    comment,  # type: str
    user_agents,  # type: list[str]
):
    """
    Create .htaccess config to block User-Agents.

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
    conf += "<IfModule mod_rewrite.c>\n"
    conf += "    RewriteEngine on\n"

    for user_agent in user_agents:
        conf += "    " + create_user_agent_line(user_agent)
        conf += "    RewriteRule . - [R=403,L]\n"

    conf += "</IfModule>"

    return conf
