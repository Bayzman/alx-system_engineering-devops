#!/usr/bin/python3

""" A recursive function that queries the Reddit API, parses the title\
    of all hot articles, and prints a sorted count of given\
    keywords (case-insensitive, delimited by spaces. Javascript\
    should count as javascript, but java should not
"""

import requests


def count_words(subreddit, word_list):
    """ A recursive function """
    url = 'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Bayzman'}
    params = {'limit': 100}
    after = None
    word_counts = None

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    posts = response.json().get('data').get('children')
    word_counts = word_counts or {}
    for post in posts:
        title = post['data']['title']
        for word in word_list:
            if word.lower() in title.lower():
                word_counts[word.lower()] = word_counts.get(word.lower(),
                                                            0) + 1
    after = response.json()['data']['after']

    if after is None:
        if not word_counts:
            pass
        for key, value in sorted(word_counts.items(),
                                 key=lambda x: (-x[1], x[0])):
            print('{}: {}'.format(key.lower(), value))
        pass

    return count_words(subreddit, word_list, after, word_counts)
