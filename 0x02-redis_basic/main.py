#!/usr/bin/env python3
"""
Main test file for Cache
"""
Cache = __import__('exercise').Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,  # store as bytes
    123: int,      # store as integer
    "bar": lambda d: d.decode("utf-8")  # store as string and decode manually
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    print(f"Stored: {value} (key: {key})")
    result = cache.get(key, fn=fn)
    print(f"Retrieved: {result}")
    assert result == value
