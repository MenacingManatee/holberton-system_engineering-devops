#!/usr/bin/python3
'''recursive function that queries the Reddit API'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    '''returns a list of all hot titles on a subreddit'''
    u_a = {'User-agent': 'User Agent 1.0'}
    if len(hot_list) >= 2 and hot_list[-1] == hot_list[-2]:
        del hot_list[-1]
        del hot_list[-1]
        if hot_list == []:
            return None
        return hot_list
    if len(hot_list) == 0:
        data = requests.get('https://reddit.com/r/{}/hot.json?limit=1'.
                            format(subreddit), headers=u_a)
        jsn = data.json().get('data')
        if jsn is None or jsn.get('children') is None:
            return None
        hot_list.append(jsn.get('children')[0].get('data').
                        get('title'))
        aft = jsn.get('after')
        hot_list = recurse(subreddit, hot_list, aft)
        return hot_list
    else:
        data = requests.get('https://reddit.com/r/{}/hot.json?after={}'
                            .format(subreddit, after), headers=u_a)
        jsn = data.json().get('data')
        if jsn is None or jsn.get('children') is None:
            return hot_list
        for item in jsn.get('children'):
            hot_list.append(item.get('data').get('title'))
#        hot_list.append(jsn.get('children')[0].get('data').
#                        get('title'))
        aft = jsn.get('after')
        hot_list = recurse(subreddit, hot_list, aft)
        return hot_list
