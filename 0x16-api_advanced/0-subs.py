#!/usr/bin/python3

""" The following function returns the number of subscribers \
    for a given subreddit
"""

import requests


def number_of_subcribers(subreddit):
    """ Returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']

        return (subs)

    else:
        return (0)
