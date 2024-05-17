#!/usr/bin/env python3
""" Main file """

Cache = __import__("exercise").Cache
replay = __import__("exercise").replay
cache = Cache()

s1 = cache.store("first")
# print(s1)
s2 = cache.store("secont")
# print(s2)
s3 = cache.store("third")
# print(s3)

length = cache._redis.llen("{}:inputs".format(cache.store.__qualname__))
inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)


print(length)
print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))

replay(cache.store)

for input, output in zip(inputs, outputs):
    print(f"{input} -> {output}")
# inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
# outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)
