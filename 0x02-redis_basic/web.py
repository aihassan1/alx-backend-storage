#!/usr/bin/env python3
""" web.py """
import requests
import redis

# from functools import wraps

# (prototype: def get_page(url: str) -> str:). The core of the function is very simple.
# It uses the requests module to obtain the HTML content of a particular URL and returns it.


def get_page(url: str) -> str:
    """get_page content"""
    r = redis.Redis()
    key = f"count:{url}"
    count = r.incr(key)
    r.expire(key, 10)
    response = requests.get(url)
    
    return response
