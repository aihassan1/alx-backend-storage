#!/usr/bin/env python3
""" web.py """
import requests
import redis


def get_page(url: str) -> str:
    """get_page content"""
    r = redis.Redis()
    key = f"count:{url}"
    count = r.incr(key)
    r.expire(key, 10)
    response = requests.get(url)

    return response
