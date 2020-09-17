#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers
for a given subreddit'''
import requests


def number_of_subscribers(subreddit):
    '''returns the number of subscribers, or 0 if invalid'''
    user_agent = {'User-agent': 'User Agent 1.0'}
    jsn = requests.get('https://reddit.com/r/{}/about.json'.format(subreddit),
                       headers=user_agent)
    data = jsn.json().get('data')
    if data is None or data.get('subscribers') is None:
        return 0
    else:
        return data.get('subscribers')
