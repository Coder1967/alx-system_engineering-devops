#!/usr/bin/python3
"""
 a recursive function that queries the Reddit API and returns a list
 containing the titles of all hot articles for a given subreddit.
 If no results are found for the given subreddit,
 the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """
    definition of the above descriped function
    """
    headers = {"User-Agent": "Mozilla/5.0 (platform; rv:geckoversion)\
Gecko/geckotrail Firefox/firefoxversion"}
    params = {
            "limit": 50,
            "after": after,
            "count": count
            }

    r = requests.get("https://www.reddit.com/r/{}/hot/.json".format(subreddit),
                     params=params, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    res = r.json().get("data")
    count += res.get("dist")
    after = res.get("after")
    for child in res.get("children"):
        #hot_list.append(child.get("data").get("title"))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, count, after)
