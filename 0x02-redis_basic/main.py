#!/usr/bin/env python3
""" Test for get_page with Redis """

from web import get_page
import redis

r = redis.Redis()

url = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://example.com"

# First request — slow and uncached
print(get_page(url))

# Second request — fast from cache
print(get_page(url))

# Check counter
print("Access count:", r.get(f"count:{url}").decode())
