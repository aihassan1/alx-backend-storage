#!/usr/bin/env python3
""" Cache class """
import redis
import uuid


class Cache:
    def __init__(self):
        """the init function"""
        self._redis = redis.Redis()
        self._redis.flushall()

    def store(self, data):
        """store data to cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
