#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__("exercise").Cache

cache = Cache()

data = 155155
key = cache.store(data)
print(key)

# local_redis = redis.Redis()
# print(local_redis.get(key))

value = cache.get(key, int)
print(value)


#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
