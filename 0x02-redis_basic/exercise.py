#!/usr/bin/env python3
"""Defines a Cache class to store data in Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class to interact with Redis storage"""

    def __init__(self):
        """Initialize Redis connection and flush database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key, store the data in Redis using the key,
        and return the key as a string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
