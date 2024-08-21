#!/usr/bin/python3

""" This is a recursive function that queries the Reddit API and\
    returns a list containing the titles of all hot articles\
    for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[]):
    """ A recursive function """
    url = "https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Bayzman'}
    params = {'limit': 100, 'after': None}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    else:
        data = response.json()
        posts = data['data']['children']

        if len(posts) == 0:
            if len(hot_list) == 0:
                return None
            else:
                return hot_list

        else:
            for post in posts:
                hot_list.append(post['data']['title'])
            params['after'] = data['data']['after']

            return recurse(subreddit, hot_list)
