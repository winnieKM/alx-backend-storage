#!/usr/bin/env python3
"""
Main file to test Cache class
"""

import redis
from exercise import Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print("Stored key:", key)

# Check if the data is stored in Redis
local_redis = redis.Redis()
print("Stored value:", local_redis.get(key))
