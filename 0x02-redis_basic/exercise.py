#!/usr/bin/env python3
"""
Module: exercise.py
Defines a Cache class that connects to Redis and performs basic caching.
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called.
    Uses Redis to increment the count for the method's qualified name.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)  # increment the call count
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    A class for interacting with Redis for simple caching operations.
    """

    def __init__(self):
        """
        Initializes the Cache class, connects to Redis and clears the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a randomly generated key.

        Args:
            data: Data to store (str, bytes, int, or float)

        Returns:
            The key as a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis and optionally converts it using `fn`.

        Args:
            key: Redis key
            fn: Optional function to apply to the returned value

        Returns:
            The original value, possibly transformed, or None if the key doesn’t exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string from Redis.

        Args:
            key: Redis key

        Returns:
            Decoded string value, or None
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer from Redis.

        Args:
            key: Redis key

        Returns:
            Integer value, or None
        """
        return self.get(key, fn=int)
