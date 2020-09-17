#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers
for a given subreddit'''
import requests


def top_ten(subreddit):
    '''returns the top 10 posts on hot for a subreddit'''
    user_agent = {'User-agent': 'User Agent 1.0'}
    jsn = requests.get('https://reddit.com/r/{}/hot.json?limit=1'.
                       format(subreddit), headers=user_agent)

    res = []
    data = jsn.json().get('data')
    if data is None or data == {}:
        print('None')
        exit
    res.append(jsn.json().get('data').get('children')[0].get('data').
               get('title'))
    for i in range(9):
        data = jsn.json().get('data')
        if data is None or data == {}:
            print('None')
            exit
        after = jsn.json().get('data').get('after')
        jsn = requests.get('https://reddit.com/r/{}/hot.json?limit=1&after={}'.
                           format('programming', after), headers=user_agent)
        res.append(jsn.json().get('data').get('children')[0].get('data').
                   get('title'))
    [print(i) for i in res]
