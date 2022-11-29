#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """definition of the function described above"""
    i = 0
    headers = {"User-Agent": "Mozilla/5.0 (platform; rv:geckoversion) \
Gecko/geckotrail Firefox/firefoxversion"}
    params = {"limit": 10}

    r = requests.get("https://www.reddit.com/r/{}/hot/.json".format(subreddit),
                     params=params, headers=headers, allow_redirects=False)
    while i < 10:
        print(r.json()["data"]["children"][i]["data"]["title"])
        i += 1
