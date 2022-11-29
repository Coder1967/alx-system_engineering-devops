#!/usr/bin/python3
"""
a function that queries the Reddit API and return
the number of subscribers (not active users, total subscribers)
for a given subreddit. If an
invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """ definition of the function described above"""
    headers = {"User-Agent": 'Mozilla/5.0 (platform; rv:geckoversion)\
Gecko/geckotrail Firefox/firefoxversion'}

    r = requests.get("https://www.reddit.com/r/{}/about.json".format(
                       subreddit),
                     headers=headers, allow_redirects=False)
    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0
