#!/usr/bin/env python3
"""Redis Cache module"""

import redis
import uuid
from typing import Union


class Cache:
    """Cache class for storing data in Redis"""

    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis under a randomly generated key.

        Args:
            data (str | bytes | int | float): The data to store.

        Returns:
            str: The generated key as a string.
        """
        key = str(uuid.uuid4())  # Generate random unique key
        self._redis.set(key, data)  # Store data in Redis
        return key
