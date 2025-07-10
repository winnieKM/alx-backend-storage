#!/usr/bin/env python3
"""Main test script for the Cache class"""
import redis
from exercise import Cache

cache = Cache()
data = b"hello"
key = cache.store(data)

print("Stored key:", key)

local_redis = redis.Redis()
print("Stored value:", local_redis.get(key))
