#!/usr/bin/python3

""" Prints the titles of the first 10 hot posts listed \
    for a given subreddit
"""

import requests
from requests.auth import HTTPBasicAuth


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed
        for a given subreddit
    """
    basic = HTTPBasicAuth('user', 'pass')
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, auth=basic, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()
        posts = posts['data']['children'][:10]
        for post in posts:
            print(post['data']['title'])
            # print(post.get('data').get('title'))
    else:
        print(None)
