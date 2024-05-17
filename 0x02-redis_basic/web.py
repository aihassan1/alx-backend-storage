#!/usr/bin/env python3
""" web.py """
import requests
import redis


def get_page(url: str) -> str:
    """get_page content"""
    r = redis.Redis()
    key = f"count:{url}"
    content_key = f"{url}"
    r.incr(key)
    
    


    if r.exists(content_key):
        print("returning cached content")
        return r.get(content_key).decode("utf-8")

    else:
        print("making a new request")
        response = requests.get(url)
        r.set(content_key, response.text, 10)
        return response.text



get_page("http://slowwly.robertomurray.co.uk")
