#!/usr/bin/env python3
""" Cache class """
import redis
import uuid
from typing import Any, Callable, Optional, Union
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """counts the number the method is called"""

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        key = f"{fn.__qualname__}"
        self._redis.incr(key)
        return fn(self, *args, **kwargs)

    return wrapper


class Cache:
    def __init__(self):
        """the init function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data to cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[callable] = None) -> Any:
        """get function to get values from db"""
        if not key:
            return None

        value = self._redis.get(key)
        if not value:
            return None

        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if fn is callable(fn):
            return fn(value)

        return value

    def get_str(self, data: bytes) -> str:
        """returns a str"""
        return data.decode("utf-8")

    def get_int(self, data):
        return int(data.decode("utf-8"))
