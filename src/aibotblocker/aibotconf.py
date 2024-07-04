#!/bin/python3

"""
Ichido AI Bot Config Builder.
"""

import argparse
import json
import os
import os.path
import aibotblocker.conf
import aibotblocker.firewalls.iptables
import aibotblocker.servers.apache
import aibotblocker.servers.caddy
import aibotblocker.servers.iis
import aibotblocker.servers.lighttpd
import aibotblocker.servers.nginx
import aibotblocker.sources.aws
import aibotblocker.sources.azure
import aibotblocker.sources.dark_visitors
import aibotblocker.sources.gcp
import aibotblocker.standards.robots


def create_config(
    path,  # type: str
    name,  # type: str
    comment,  # type: str
    fn,  # type: Callable
    values,  # type: list[str]
):
    """
    Dispatch function to create config files.

    :param path: Path to the output dir.
    :type path: str
    :param name: Name of the config file.
    :type name: str
    :param comment: Config file comment.
    :type comment: str
    :param fn: Create config function.
    :type fn: Callable
    :param values: values passed into the callable.
    :type values: Callable
    """
    conf_path = os.path.join(path, name + "-block-ai-bots.conf")

    with open(conf_path, "w") as conf_file:
        conf = fn(comment, values)
        conf_file.write(conf)


def main():
    # Parse args.
    parser = argparse.ArgumentParser(
        description="",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="_build",
        help="Directory where config files will be outputted. Default is `_build`.",
    )
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default="recommended",
        help="Config used, either (recommended | nonrecommended). Default is `recommended`.",
    )
    parser.add_argument(
        "-m",
        "--custom",
        type=str,
        help="Custom config. Must be JSON formatted string. See `conf.py` for the format.",
    )
    args = vars(parser.parse_args())

    output_dir = args["output"]
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    if args["custom"] is not None:
        config = json.loads(args["custom"])
    else:
        config = aibotblocker.conf.conf[args["config"]]

    ips = []
    user_agents = []

    # Include custom values.
    if "ips" in config and "include" in config["ips"]:
        ips += config["ips"]["include"]

    if "user_agents" in config and "include" in config["user_agents"]:
        user_agents += config["user_agents"]["include"]

    # Download data sources.
    if "dark_visitors" in config["sources"]:
        user_agents += aibotblocker.sources.dark_visitors.fetch_agents(
            config["categories"]["exclude"]
        )

    if "aws" in config["sources"]:
        ips += aibotblocker.sources.aws.fetch_ips()

    if "azure" in config["sources"]:
        ips += aibotblocker.sources.azure.fetch_ips()

    if "gcp" in config["sources"]:
        ips += aibotblocker.sources.gcp.fetch_ips()

    # Remove duplicates.
    ips = set(ips)
    user_agents = set(user_agents)

    # Remove excluded values.
    if "ips" in config and "exclude" in config["ips"]:
        for ip in config["ips"]["exclude"]:
            if ip in ips:
                ips.remove(ip)

    if "user_agents" in config and "exclude" in config["user_agents"]:
        for user_agent in config["user_agents"]["exclude"]:
            if user_agent in user_agents:
                user_agents.remove(user_agent)

    # Sort values.
    user_agents = list(sorted(list(user_agents)))
    ips = list(sorted(list(ips)))

    # Build configs.
    comment = config["comment"]

    create_config(
        output_dir,
        args["config"] + "-apache",
        comment,
        aibotblocker.servers.apache.create_config,
        user_agents,
    )
    create_config(
        output_dir,
        args["config"] + "-htaccess",
        comment,
        aibotblocker.servers.apache.create_htaccess_config,
        user_agents,
    )
    create_config(
        output_dir,
        args["config"] + "-caddy",
        comment,
        aibotblocker.servers.caddy.create_config,
        user_agents,
    )
    create_config(
        output_dir,
        args["config"] + "-iis",
        comment,
        aibotblocker.servers.iis.create_config,
        user_agents,
    )
    create_config(
        output_dir,
        args["config"] + "-iptables",
        comment,
        aibotblocker.firewalls.iptables.create_config,
        ips,
    )
    create_config(
        output_dir,
        args["config"] + "-lighttpd",
        comment,
        aibotblocker.servers.lighttpd.create_config,
        user_agents,
    )
    create_config(
        output_dir,
        args["config"] + "-nginx",
        comment,
        aibotblocker.servers.nginx.create_config,
        user_agents,
    )
    create_config(
        output_dir,
        args["config"] + "-robots",
        comment,
        aibotblocker.standards.robots.create_config,
        user_agents,
    )


if __name__ == "__main__":
    main()
