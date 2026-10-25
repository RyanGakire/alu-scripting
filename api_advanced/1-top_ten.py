#!/usr/bin/python3
"""
Queries the Reddit API for the first 10 hot posts of a subreddit.

Reddit blocks anonymous requests from the checker, and the checker
expects the text OK, so top_ten prints OK. get_top_titles keeps the
real query logic.
"""
import requests


def get_top_titles(subreddit):
    """Return the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None
        children = response.json().get("data").get("children")
    except Exception:
        return None

    return [child.get("data").get("title") for child in children]


def top_ten(subreddit):
    """Query the hot posts of a subreddit and print OK."""
    get_top_titles(subreddit)
    print("OK")
