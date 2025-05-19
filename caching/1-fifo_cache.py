#!/usr/bin/env python3


"""
FIFO caching system that inherits from BaseCaching.
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching and is a caching system."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            if key is not
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.queue.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item
    def get(self, key):
        """Get an item by key."""
        if key is not None:
            return self.cache_data.get(key, None)
        return None
