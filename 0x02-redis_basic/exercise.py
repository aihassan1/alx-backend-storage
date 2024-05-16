#!/usr/bin/env python3
""" Cache class """
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """the init function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, float, str, bytes]) -> str:
        """store data to cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
