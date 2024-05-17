#!/usr/bin/env python3
""" Cache class """
import redis
import uuid
from typing import Any, Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count number of calls made to a method"""
    key = method.__qualname__

    @wraps(method)
    def counter(self, *args, **kwargs):
        """decorator method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return counter


# DEFINE call history dicorator
# input will be stored in a list
# output will be stored in a list for each method


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function."""
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def history(self, *args):
        """Append input & output to Redis list"""
        self._redis.rpush(input_key, str(args))
        output = method(self, *args)
        self._redis.rpush(output_key, str(output))
        return output

    return history


class Cache:
    def __init__(self):
        """the init function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data to cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
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
        if fn is callable(fn) and fn is not None:
            return fn(value)

        return value

    def get_str(self, data: bytes) -> str:
        """returns a str"""
        return data.decode("utf-8")

    def get_int(self, data):
        return int(data.decode("utf-8"))
