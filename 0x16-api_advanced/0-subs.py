#!/usr/bin/python3

""" The following function returns the number of subscribers \
    for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Bayzman"}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code != 200:
        return 0

    else:
        data = response.json()
        subs = data['data']['subscribers']
        return subs

#subscribers = number_of_subscribers('python')
#print('The number of subscribers in r/python is: {}'.format(subscribers))
