#!/usr/bin/env python3
""" web.py """
import requests
import redis
from typing import Callable
from functools import wraps


def cacher(method: Callable) -> str:
    """cacher function"""

    @wraps(method)
    def wrapper(url: str) -> str:
        r = redis.Redis()
        key = f"count:{url}"
        r.incr(key)
        cached_page = r.get(url)

        if cached_page:
            return cached_page.decode("utf-8")
        response = method(url)
        r.set(url, response, 10)
        return response

    return wrapper


@cacher
def get_page(url: str) -> str:
    """get_page content"""

    response = requests.get(url)
    return response.text
