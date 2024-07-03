"""
Prebuilt configs.
"""

conf = {
    "minimal": {
        "comment": "Ichido AI Bot Blocker.",
        "sources": [
            "dark_visitors",
            "aws",
            "gcp",
        ],
        "categories": {
            "exclude": [
                "Archivers",
                "Developer Helper",
                "Fetcher",
                "Search Engine Crawler",
            ]
        },
        "ips": {
            "include": [],
            "exclude": [],
        },
        "user_agents": {
            "include": [
                "ImagesiftBot",
            ],
            "exclude": [
                "Atom Feed Robot",
                "AwarioRssBot",
                "CCBot",
                "Feedbin",
                "feedbot",
                "Feedspot",
                "FeedValidator",
                "Google-Extended",
                "NAVER Blog Rssbot",
                "page2rss",
                "rssbot",
                "RSSingBot",
                "search.marginalia.nu",
            ],
        },
    },
    "full": {
        "comment": "Ichido AI Bot Blocker.",
        "sources": [
            "dark_visitors",
            "aws",
            "gcp",
        ],
        "categories": {"exclude": []},
        "ips": {
            "include": [],
            "exclude": [],
        },
        "user_agents": {
            "include": [
                "ImagesiftBot",
            ],
            "exclude": [
                "Google-Extended",
            ],
        },
    },
}
