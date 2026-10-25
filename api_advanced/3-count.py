#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of the given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """Print how many times each keyword appears in hot article titles."""
    if word_count is None:
        word_count = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_student)"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
    except Exception:
        return

    # Count every word of every title on this page (in lowercase)
    for child in data.get("children", []):
        title = child.get("data", {}).get("title", "")
        for token in title.lower().split():
            word_count[token] = word_count.get(token, 0) + 1

    # More pages left: call the function again with the next page
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, word_count)

    # Last page reached: add up the keywords (duplicates are summed)
    totals = {}
    for word in word_list:
        word = word.lower()
        if word_count.get(word, 0) > 0:
            totals[word] = totals.get(word, 0) + word_count.get(word)

    # Sort by count (highest first), then alphabetically
    for word, total in sorted(totals.items(),
                              key=lambda item: (-item[1], item[0])):
        print("{}: {}".format(word, total))
