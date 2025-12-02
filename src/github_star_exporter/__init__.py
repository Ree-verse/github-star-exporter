"""
github-star-exporter | https://github.com/ree-verse/github-star-exporter

Copyright © 2025 Ree-verse. All rights reserved.
Licensed under the MIT License. See LICENSE in the project root for license information.
"""

__all__ = ["__version__", "arg_parser", "colorize", "export_starred_repos"]
__version__ = "1.0.0"
__author__ = "Ree-verse"
__license__ = "MIT"
__doc__ = "github-star-exporter - Export (your) GitHub starred repositories to a JSON file."

import argparse
import json
import os
import time
from pathlib import Path
from typing import Dict, List, Optional

import requests
from colorama import Fore, Style

if os.name == "nt":
    from colorama import just_fix_windows_console

    just_fix_windows_console()


def colorize(text: str, color: str) -> str:
    """Returns the given text with the specified color."""
    return f"{color}{text}{Style.RESET_ALL}"


def fetch_starred_repos(token: str, target_user: Optional[str]) -> List[Dict]:
    """Fetches all starred repos for a user via GitHub REST API."""
    url = f"https://api.github.com/users/{target_user}/starred" if target_user else "https://api.github.com/user/starred"
    repos = []

    while url:
        response = requests.get(
            url,
            headers={
                "Authorization": f"token {token}",
                "Accept": "application/vnd.github.v3+json",
            },
            params={"per_page": 100},
        )

        if response.status_code == 401:
            raise ValueError(colorize("Bad credentials", Fore.RED))
        if response.status_code != 200:
            raise requests.HTTPError(
                colorize(
                    f"GitHub API error: {response.status_code}, {response.text}",
                    Fore.RED,
                )
            )

        data = response.json()
        for repo in data:
            repos.append(
                {
                    "name": repo["name"],
                    "full_name": repo["full_name"],
                    "private": repo["private"],
                    "html_url": repo["html_url"],
                    "description": repo["description"],
                    "fork": repo["fork"],
                    "homepage": repo["homepage"],
                    "language": repo["language"],
                    "forks_count": repo["forks_count"],
                    "stargazers_count": repo["stargazers_count"],
                    "topics": repo.get("topics", []),
                    "archived": repo["archived"],
                    "visibility": repo["visibility"],
                    "owner": repo["owner"]["login"],
                    "pushed_at": repo["pushed_at"],
                    "created_at": repo["created_at"],
                    "updated_at": repo["updated_at"],
                    "license_name": repo["license"]["name"] if repo.get("license") else "",
                }
            )
        url = response.links.get("next", {}).get("url")

    return repos


def export_starred_repos(token: str, target_user: Optional[str], output_path: str = "output.json") -> None:
    """Exports all starred repos into a JSON file (with information)."""
    print(
        colorize(
            f"Fetching starred repositories for {'user ' + target_user if target_user else 'authenticated user'}...",
            Fore.CYAN,
        )
    )

    start_time = time.monotonic()
    starred_repos = fetch_starred_repos(token, target_user)
    duration = time.monotonic() - start_time

    try:
        Path(output_path).write_text(
            json.dumps(starred_repos, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )
    except OSError as e:
        raise OSError(
            colorize(
                f"Error writing to file {output_path}: {e}",
                Fore.RED,
            )
        )

    print(
        colorize(
            f"Export completed in {duration:.2f}s to: {output_path} ({len(starred_repos)} repos)",
            Fore.GREEN,
        )
    )


def arg_parser() -> argparse.ArgumentParser:
    """Builds and configures the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="github-star-exporter",
        description="Export (your) GitHub starred repositories to a JSON file.",
    )

    options = [
        (
            ["-t", "--token"],
            {"type": str, "help": "GitHub access token (needs read:user permission)"},
        ),
        (
            ["-u", "--user"],
            {
                "type": str,
                "help": "Target GitHub username (default: authenticated user)",
            },
        ),
        (
            ["-o", "--output"],
            {
                "type": str,
                "default": "output.json",
                "help": "Output JSON file (default: output.json)",
            },
        ),
        (
            ["-v", "--version"],
            {"action": "store_true", "help": "Version information"},
        ),
    ]

    for flags, kwargs in options:
        parser.add_argument(*flags, **kwargs)

    return parser.parse_args()
