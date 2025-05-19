#!/usr/bin/env python3

"""
basic cache module that uses a simple caching system
without limitations.
"""


from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching and is a caching system."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key."""
        if key is not None:
            return self.cache_data.get(key, None)
        return None
