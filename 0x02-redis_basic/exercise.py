#!/usr/bin/env python3
"""
Module to define the Cache class for Redis operations.
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    A simple Cache class that connects to Redis and stores/retrieves data.
    """

    def __init__(self):
        """
        Initialize the Redis client and clear the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key.

        Args:
            data: str, bytes, int, or float to store.

        Returns:
            The generated key as a string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key and apply an optional conversion function.

        Args:
            key: The key to look up in Redis.
            fn: A callable function that converts the data (e.g., bytes to str or int).

        Returns:
            The data after applying fn, or the raw data if fn is None.
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value
