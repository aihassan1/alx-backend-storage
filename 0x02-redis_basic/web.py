#!/usr/bin/env python3
""" web.py """
import requests
import redis


def get_page(url: str) -> str:
    """get_page content"""
    r = redis.Redis()
    key = f"count:{url}"
    r.incr(key)
    response = requests.get(url)

    return response.text
