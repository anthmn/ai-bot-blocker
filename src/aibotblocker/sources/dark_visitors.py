"""
Dark Visitor User-Agent fetcher.
"""

import re
import urllib.request


def parse_agents(
    html,  # type: str
):
    """
    Parse Dark Visitor User-Agents.

    :param data: Page HTML.
    :type data: str
    :return: Bot User-Agents.
    :rtype: list[str]
    """
    agent_re = re.compile('<div class="name agent-name">.*?</div>', re.DOTALL)
    agents = agent_re.findall(html)
    agents = list(map(lambda agent: agent[29:-6].strip(), agents))

    return agents


def parse_categories(
    html,  # type: str
):
    """
    Parse Dark Visitor categories.

    :param data: Page HTML.
    :type data: str
    :return: Bot categories.
    :rtype: list[str]
    """
    category_re = re.compile('<div class="tag" style=".*?">.*?</div>', re.DOTALL)
    categories = category_re.findall(html)
    categories = list(
        map(lambda category: category[:-6].split(">")[1].strip(), categories)
    )

    return categories


def fetch_agents(
    category_excludes,  # type: list[str]
):
    """
    Fetch Dark Visitors bot User-Agent data.

    :param category_excludes: Bot catorgies that will be excluded.
    :type category_excludes: set[str]
    :return: Dark Visitor User-Agents.
    :rtype: list[str]
    """
    url = "https://darkvisitors.com/agents"

    with urllib.request.urlopen(url) as response:
        html = response.read().decode()

    agents = parse_agents(html)
    categories = parse_categories(html)
    user_agents = []

    category_excludes_set = set(category_excludes)
    for i in range(len(agents)):
        if categories[i] in category_excludes_set:
            continue

        user_agents.append(agents[i])

    return user_agents
