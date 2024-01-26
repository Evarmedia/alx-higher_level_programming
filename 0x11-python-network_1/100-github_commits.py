#!/usr/bin/python3
"""Module to get commit hashes from github user"""

import requests
from sys import argv


def pulls_gitcommits_from_repo():
    """Displays the last 10 commits from a github user"""
    if len(argv) < 3:
        print(f"usage: {argv[0]} <repository> <userName>")
        exit(1)

    repoName, userName = argv[1], argv[2]
    ur_url = f"https://api.github.com/repos/{userName}/{repoName}/commits"
    try:
        commits = requests.get(ur_url, {"Accept": "application/vnd.github+json"})
        commits.raise_for_status()
        commits = commits.json()
        for commit in commits[:10]:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    except requests.exceptions.HTTPError as e:
        print(f"[{commits.status_code}] {e}")


if __name__ == "__main__":
    pulls_gitcommits_from_repo()
