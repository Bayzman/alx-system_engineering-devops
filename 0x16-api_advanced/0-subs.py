#!/usr/bin/python3

""" The following function returns the number of subscribers \
    for a given subreddit
"""

import requests
from requests.auth import HTTPBasicAuth


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    basic = HTTPBasicAuth('user', 'pass')
    response = requests.get(url, auth=basic, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']
        return subs

    else:
        return 0
