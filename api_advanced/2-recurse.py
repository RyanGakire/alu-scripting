#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list with the titles
of all hot articles of a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot article titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get("data", {})
    except Exception:
        return None

    titles = [child.get("data", {}).get("title")
              for child in data.get("children", [])]
    hot_list = hot_list + titles

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)

    if len(hot_list) == 0:
        return None
    return hot_list
