#!/usr/bin/env python3
"""
web.py
Fetches a URL and caches it in Redis with expiration.
Tracks how many times a URL was accessed.
"""

import redis
import requests
from typing import Callable
from functools import wraps

# Connect to local Redis
r = redis.Redis()


def count_access(method: Callable) -> Callable:
    """
    Decorator to count how many times a URL has been accessed.
    """

    @wraps(method)
    def wrapper(url: str) -> str:
        count_key = f"count:{url}"
        r.incr(count_key)
        return method(url)

    return wrapper


def cache_result(method: Callable) -> Callable:
    """
    Decorator to cache the result of the URL for 10 seconds.
    """

    @wraps(method)
    def wrapper(url: str) -> str:
        cache_key = f"cached:{url}"
        cached_data = r.get(cache_key)

        if cached_data:
            return cached_data.decode('utf-8')

        # Fetch and cache
        result = method(url)
        r.setex(cache_key, 10, result)
        return result

    return wrapper


@count_access
@cache_result
def get_page(url: str) -> str:
    """
    Retrieves the HTML content of a URL and caches it.
    """
    response = requests.get(url)
    return response.text
