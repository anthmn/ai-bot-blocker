conf = {
    "minimal": {
        "comment": "Ichido AI Bot Blocker.",
        "sources": [
            "dark_visitors",
            "aws",
            "azure",
            "gcp",
        ],
        "categories": {
            "exclude": [
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
                "Google-Extended",
                "search.marginalia.nu",
            ],
        },
    },
    "full": {
        "comment": "Ichido AI Bot Blocker.",
        "sources": [
            "dark_visitors",
            "aws",
            "azure",
            "gcp",
        ],
        "categories": {
            "exclude": [
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
                "Google-Extended",
                "search.marginalia.nu",
            ],
        },
    },
}
