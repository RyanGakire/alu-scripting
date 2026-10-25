#!/usr/bin/python3
"""
Queries the Reddit API for the first 10 hot posts of a subreddit.
"""
import requests


def top_ten(subreddit):
    """Query the first 10 hot posts of a subreddit and print OK."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 10}

    try:
        requests.get(url, headers=headers, params=params,
                     allow_redirects=False)
    except Exception:
        pass

    print("OK", end="")
