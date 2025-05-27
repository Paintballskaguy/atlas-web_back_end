#!/usr/bin/env python3

"""
A caching system that implements the MRU (Most Recently Used) eviction policy.
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A caching system that implements the MRU (Most Recently Used) policy.
    """
    def __init__(self):
        """Initialize the MRU eviction policy"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """add an item to the cache following the MRU policy"""
        if key is None or item is None:
            return # do nothing if key or item is None.
        if key is self.cache_data:
            # Update existing item and move to MRU position.    
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # removes most recently used item
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """"Retrieve an item from the cache and update its usage."""
        if key is not None and key in self.cache_data:
            # Update the usage order
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
