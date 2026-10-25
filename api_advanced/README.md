# API advanced

Python functions that query the Reddit API with the `requests` module.
Each request sends a custom `User-Agent` and does not follow redirects,
so an invalid subreddit is detected instead of landing on a search page.

## Files

| File | Description |
| ---- | ----------- |
| `0-subs.py` | `number_of_subscribers(subreddit)` returns the total number of subscribers of a subreddit, or `0` if it is invalid. |
| `1-top_ten.py` | `top_ten(subreddit)` prints the titles of the first 10 hot posts of a subreddit, or `None` if it is invalid. |
| `2-recurse.py` | `recurse(subreddit, hot_list=[])` recursively goes through every page of hot posts and returns a list of all titles, or `None` if the subreddit is invalid. |
| `3-count.py` | `count_words(subreddit, word_list)` recursively goes through all hot posts and prints how many times each keyword appears in the titles, sorted by count (highest first) then alphabetically. |

## Usage

```
$ python3 0-main.py programming
756024
$ python3 1-main.py this_is_a_fake_subreddit
None
$ python3 3-main.py programming 'python java javascript'
java: 27
javascript: 20
python: 17
```

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- `requests` module
- PEP 8 style
