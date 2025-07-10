#!/usr/bin/env python3
"""
Test file for Cache class get method.
"""

from exercise import Cache

cache = Cache()

# Store a string
key_str = cache.store("Hello Redis")
print("Raw:", cache.get(key_str))               # Should print b'Hello Redis'
print("As str:", cache.get(key_str, str))       # Should print 'Hello Redis'

# Store an integer
key_int = cache.store(123)
print("Raw:", cache.get(key_int))               # Should print b'123'
print("As int:", cache.get(key_int, int))       # Should print 123
